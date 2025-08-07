from abc import ABC, abstractmethod
import pandas as pd
import random
from typing import List, Dict, Any, Optional, Tuple

class MaterialDatabase(ABC):
    """
    Abstract base class for all material databases in EMOS.
    Defines the standard interface that all database implementations must follow.
    """
    
    def __init__(self, name: str):
        """Initialize the database with a name."""
        self.name = name
        self._dataset = None
        self._properties_units = {}
        self._initialize_database()
    
    @abstractmethod
    def _initialize_database(self):
        """Initialize the database with properties, units, and sample data."""
        pass
    
    def get_available_properties(self) -> Dict[str, str]:
        """
        Returns a dictionary of available material properties and their units.
        
        Returns:
            Dict[str, str]: Dictionary where keys are property names and values are units
        """
        return self._properties_units.copy()
    
    def query_materials(self, 
                       property_filters: Dict[str, Any], 
                       max_count: int = 100) -> pd.DataFrame:
        """
        Query materials based on property filters and return at most max_count results.
        
        Args:
            property_filters: Dictionary of property names and their target values
            max_count: Maximum number of materials to return
            
        Returns:
            pd.DataFrame: Filtered dataset containing matching materials
        """
        if self._dataset is None or self._dataset.empty:
            return pd.DataFrame()
        
        filtered_data = self._dataset.copy()
        
        # Apply filters
        for property_name, target_value in property_filters.items():
            if property_name in filtered_data.columns:
                # Handle different types of filtering
                if isinstance(target_value, (int, float)):
                    # Numerical filtering with tolerance
                    tolerance = abs(target_value * 0.1)  # 10% tolerance
                    filtered_data = filtered_data[
                        abs(filtered_data[property_name] - target_value) <= tolerance
                    ]
                elif isinstance(target_value, str):
                    # String filtering
                    filtered_data = filtered_data[
                        filtered_data[property_name].str.contains(target_value, case=False, na=False)
                    ]
        
        # Return at most max_count results
        return filtered_data.head(max_count)
    
    @property
    def dataset(self) -> pd.DataFrame:
        """Get the full dataset."""
        return self._dataset.copy() if self._dataset is not None else pd.DataFrame()
    
    def get_database_info(self) -> Dict[str, Any]:
        """Return general information about the database."""
        return {
            "name": self.name,
            "total_materials": len(self._dataset) if self._dataset is not None else 0,
            "properties_count": len(self._properties_units),
            "properties": list(self._properties_units.keys())
        }
