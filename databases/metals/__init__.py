import pandas as pd
import numpy as np
from ..import MaterialDatabase

class MetalsDatabase(MaterialDatabase):
    """
    Database for metallic materials and alloys.
    Focuses on mechanical, thermal, and electrical properties of metals.
    """
    
    def __init__(self):
        super().__init__("Metals and Alloys Database")
    
    def _initialize_database(self):
        """Initialize the metals database with relevant properties and sample data."""
        # Define properties and their units
        self._properties_units = {
            "material_name": "string",
            "density": "g/cm³",
            "melting_point": "°C",
            "thermal_conductivity": "W/m·K",
            "electrical_resistivity": "µΩ·cm",
            "young_modulus": "GPa",
            "yield_strength": "MPa",
            "ultimate_tensile_strength": "MPa",
            "hardness_hv": "HV",
            "thermal_expansion": "10⁻⁶/K",
            "poisson_ratio": "dimensionless",
            "crystal_structure": "string",
            "magnetic_property": "string"
        }
        
        # Generate sample data
        np.random.seed(42)  # For reproducible results
        n_materials = 150
        
        metal_names = [
            "Steel-304", "Aluminum-6061", "Copper-C101", "Titanium-Grade2", "Brass-360",
            "Bronze-C932", "Inconel-718", "Hastelloy-C276", "Monel-400", "Nickel-200",
            "Zinc-Alloy-3", "Magnesium-AZ91", "Lead-Chemical", "Tin-Pure", "Silver-999"
        ]
        
        crystal_structures = ["FCC", "BCC", "HCP", "Tetragonal", "Orthorhombic"]
        magnetic_properties = ["Ferromagnetic", "Paramagnetic", "Diamagnetic", "Antiferromagnetic"]
        
        data = []
        for i in range(n_materials):
            material = {
                "material_name": np.random.choice(metal_names) + f"-Variant{i%10}",
                "density": np.random.uniform(2.5, 19.3),
                "melting_point": np.random.uniform(300, 3400),
                "thermal_conductivity": np.random.uniform(5, 400),
                "electrical_resistivity": np.random.uniform(1.6, 150),
                "young_modulus": np.random.uniform(10, 450),
                "yield_strength": np.random.uniform(50, 1500),
                "ultimate_tensile_strength": np.random.uniform(100, 2000),
                "hardness_hv": np.random.uniform(30, 800),
                "thermal_expansion": np.random.uniform(5, 25),
                "poisson_ratio": np.random.uniform(0.15, 0.45),
                "crystal_structure": np.random.choice(crystal_structures),
                "magnetic_property": np.random.choice(magnetic_properties)
            }
            data.append(material)
        
        self._dataset = pd.DataFrame(data)
    
    def get_alloy_composition(self, material_name: str) -> dict:
        """Get detailed alloy composition for a specific material."""
        # Placeholder implementation
        compositions = {
            "Fe": np.random.uniform(0, 100),
            "Cr": np.random.uniform(0, 30),
            "Ni": np.random.uniform(0, 20),
            "Mo": np.random.uniform(0, 10),
            "C": np.random.uniform(0, 2)
        }
        return {k: v for k, v in compositions.items() if v > 0.1}
