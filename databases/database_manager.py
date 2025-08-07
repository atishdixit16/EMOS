from typing import Dict, List, Any
import pandas as pd

from .metals import MetalsDatabase
from .semiconductors import SemiconductorsDatabase  
from .ceramics import CeramicsDatabase
from .polymers import PolymersDatabase

class DatabaseManager:
    """
    Manager class to handle all material databases in EMOS.
    Provides unified interface to query across multiple databases.
    """
    
    def __init__(self):
        """Initialize all available databases."""
        self.databases = {
            'metals': MetalsDatabase(),
            'semiconductors': SemiconductorsDatabase(),
            'ceramics': CeramicsDatabase(),
            'polymers': PolymersDatabase()
        }
    
    def get_available_databases(self) -> List[str]:
        """Get list of available database names."""
        return list(self.databases.keys())
    
    def get_database_info(self, db_name: str = None) -> Dict[str, Any]:
        """Get information about specific database or all databases."""
        if db_name:
            return self.databases[db_name].get_database_info()
        else:
            return {name: db.get_database_info() for name, db in self.databases.items()}
    
    def query_database(self, db_name: str, property_filters: Dict[str, Any], max_count: int = 100) -> pd.DataFrame:
        """Query a specific database."""
        if db_name not in self.databases:
            raise ValueError(f"Database '{db_name}' not found. Available: {list(self.databases.keys())}")
        
        return self.databases[db_name].query_materials(property_filters, max_count)
    
    def query_all_databases(self, property_filters: Dict[str, Any], max_count: int = 100) -> Dict[str, pd.DataFrame]:
        """Query all databases and return results organized by database."""
        results = {}
        for db_name, database in self.databases.items():
            try:
                result = database.query_materials(property_filters, max_count)
                if not result.empty:
                    results[db_name] = result
            except Exception as e:
                print(f"Error querying {db_name}: {e}")
        
        return results
    
    def get_all_properties(self) -> Dict[str, Dict[str, str]]:
        """Get all available properties from all databases."""
        return {name: db.get_available_properties() for name, db in self.databases.items()}
