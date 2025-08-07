import pandas as pd
import numpy as np
from ..import MaterialDatabase

class PolymersDatabase(MaterialDatabase):
    """
    Database for polymer materials.
    Focuses on mechanical, thermal, and processing properties.
    """
    
    def __init__(self):
        super().__init__("Polymers and Composites Database")
    
    def _initialize_database(self):
        """Initialize the polymers database with polymer-specific properties."""
        self._properties_units = {
            "material_name": "string",
            "density": "g/cm³",
            "glass_transition_temp": "°C",
            "melting_point": "°C",
            "tensile_strength": "MPa",
            "elongation_at_break": "%",
            "flexural_modulus": "GPa",
            "impact_strength": "J/m",
            "thermal_conductivity": "W/m·K",
            "specific_heat": "J/g·K",
            "dielectric_strength": "kV/mm",
            "volume_resistivity": "Ω·cm",
            "water_absorption": "%",
            "mold_shrinkage": "%",
            "polymer_type": "string",
            "crystallinity": "%",
            "molecular_weight": "g/mol"
        }
        
        np.random.seed(789)
        n_materials = 80
        
        polymer_names = [
            "PE", "PP", "PS", "PVC", "PET", "PA66", "PC", "ABS",
            "PMMA", "POM", "PTFE", "PI", "PEEK", "PPS", "LCP"
        ]
        
        polymer_types = ["Thermoplastic", "Thermoset", "Elastomer", "Composite", "Biopolymer"]
        
        data = []
        for i in range(n_materials):
            polymer_type = np.random.choice(polymer_types)
            
            # Adjust properties based on polymer type
            if polymer_type == "Thermoplastic":
                crystallinity_range = (0, 80)
                melting_range = (80, 350)
            elif polymer_type == "Thermoset":
                crystallinity_range = (0, 20)
                melting_range = (200, 400)  # Decomposition temp
            else:
                crystallinity_range = (0, 60)
                melting_range = (100, 300)
            
            material = {
                "material_name": np.random.choice(polymer_names) + f"-{i%12}",
                "density": np.random.uniform(0.8, 2.2),
                "glass_transition_temp": np.random.uniform(-100, 200),
                "melting_point": np.random.uniform(*melting_range),
                "tensile_strength": np.random.uniform(10, 200),
                "elongation_at_break": np.random.uniform(1, 800),
                "flexural_modulus": np.random.uniform(0.5, 15),
                "impact_strength": np.random.uniform(10, 1000),
                "thermal_conductivity": np.random.uniform(0.1, 2.0),
                "specific_heat": np.random.uniform(1.0, 3.0),
                "dielectric_strength": np.random.uniform(10, 50),
                "volume_resistivity": np.random.uniform(1e12, 1e18),
                "water_absorption": np.random.uniform(0.01, 5.0),
                "mold_shrinkage": np.random.uniform(0.1, 3.0),
                "polymer_type": polymer_type,
                "crystallinity": np.random.uniform(*crystallinity_range),
                "molecular_weight": np.random.uniform(10000, 1000000)
            }
            data.append(material)
        
        self._dataset = pd.DataFrame(data)
    
    def get_processing_conditions(self, material_name: str) -> dict:
        """Get recommended processing conditions for a polymer."""
        material_data = self._dataset[self._dataset['material_name'] == material_name]
        if material_data.empty:
            return {}
        
        melting_temp = material_data['melting_point'].iloc[0]
        return {
            "processing_temperature": f"{melting_temp + 20}-{melting_temp + 50} °C",
            "injection_pressure": f"{np.random.uniform(50, 150):.0f} MPa",
            "cooling_rate": f"{np.random.uniform(5, 30):.1f} °C/min",
            "mold_temperature": f"{np.random.uniform(40, 120):.0f} °C"
        }
