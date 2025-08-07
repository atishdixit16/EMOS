import pandas as pd
import numpy as np
from ..import MaterialDatabase

class CeramicsDatabase(MaterialDatabase):
    """
    Database for ceramic materials.
    Focuses on thermal, mechanical, and dielectric properties.
    """
    
    def __init__(self):
        super().__init__("Advanced Ceramics Database")
    
    def _initialize_database(self):
        """Initialize the ceramics database with relevant properties."""
        self._properties_units = {
            "material_name": "string",
            "density": "g/cm³",
            "hardness_hv": "HV",
            "fracture_toughness": "MPa·m^0.5",
            "compressive_strength": "MPa",
            "flexural_strength": "MPa",
            "thermal_conductivity": "W/m·K",
            "thermal_shock_resistance": "K",
            "dielectric_constant": "dimensionless",
            "dielectric_loss": "dimensionless",
            "coefficient_thermal_expansion": "10⁻⁶/K",
            "max_service_temperature": "°C",
            "porosity": "%",
            "grain_size": "µm",
            "ceramic_type": "string",
            "crystal_structure": "string"
        }
        
        np.random.seed(456)
        n_materials = 100
        
        ceramic_names = [
            "Al2O3", "ZrO2", "SiC", "Si3N4", "AlN", "BN", "TiC", "WC",
            "MgO", "CaO", "Y2O3", "BeO", "ThO2", "UO2", "PZT"
        ]
        
        ceramic_types = ["Oxide", "Carbide", "Nitride", "Boride", "Silicide", "Composite"]
        crystal_structures = ["Cubic", "Tetragonal", "Hexagonal", "Monoclinic", "Triclinic"]
        
        data = []
        for i in range(n_materials):
            # Different property ranges for different ceramic types
            ceramic_type = np.random.choice(ceramic_types)
            
            if ceramic_type == "Oxide":
                hardness_range = (800, 2000)
                thermal_cond_range = (2, 40)
            elif ceramic_type == "Carbide":
                hardness_range = (1500, 3000)
                thermal_cond_range = (20, 200)
            else:
                hardness_range = (1000, 2500)
                thermal_cond_range = (5, 100)
            
            material = {
                "material_name": np.random.choice(ceramic_names) + f"-Grade{i%8}",
                "density": np.random.uniform(2.0, 15.0),
                "hardness_hv": np.random.uniform(*hardness_range),
                "fracture_toughness": np.random.uniform(2, 15),
                "compressive_strength": np.random.uniform(500, 5000),
                "flexural_strength": np.random.uniform(100, 1000),
                "thermal_conductivity": np.random.uniform(*thermal_cond_range),
                "thermal_shock_resistance": np.random.uniform(200, 800),
                "dielectric_constant": np.random.uniform(4, 100),
                "dielectric_loss": np.random.uniform(0.0001, 0.1),
                "coefficient_thermal_expansion": np.random.uniform(2, 15),
                "max_service_temperature": np.random.uniform(800, 2000),
                "porosity": np.random.uniform(0, 20),
                "grain_size": np.random.uniform(0.1, 50),
                "ceramic_type": ceramic_type,
                "crystal_structure": np.random.choice(crystal_structures)
            }
            data.append(material)
        
        self._dataset = pd.DataFrame(data)
    
    def filter_by_application(self, application: str) -> pd.DataFrame:
        """Filter ceramics suitable for specific applications."""
        if application.lower() == "high_temperature":
            return self._dataset[self._dataset['max_service_temperature'] > 1500]
        elif application.lower() == "electronic":
            return self._dataset[self._dataset['dielectric_constant'] > 10]
        elif application.lower() == "structural":
            return self._dataset[self._dataset['fracture_toughness'] > 5]
        else:
            return self._dataset
