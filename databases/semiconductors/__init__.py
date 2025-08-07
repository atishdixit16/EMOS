import pandas as pd
import numpy as np
from ..import MaterialDatabase

class SemiconductorsDatabase(MaterialDatabase):
    """
    Database for semiconductor materials.
    Focuses on electronic, optical, and band structure properties.
    """
    
    def __init__(self):
        super().__init__("Semiconductors Database")
    
    def _initialize_database(self):
        """Initialize the semiconductors database with electronic properties."""
        self._properties_units = {
            "material_name": "string",
            "band_gap": "eV",
            "electron_mobility": "cm²/V·s",
            "hole_mobility": "cm²/V·s", 
            "dielectric_constant": "dimensionless",
            "refractive_index": "dimensionless",
            "lattice_constant": "Å",
            "effective_mass_electron": "m₀",
            "effective_mass_hole": "m₀",
            "breakdown_field": "MV/cm",
            "thermal_conductivity": "W/m·K",
            "crystal_system": "string",
            "semiconductor_type": "string",
            "dopant_concentration": "cm⁻³"
        }
        
        np.random.seed(123)
        n_materials = 120
        
        semiconductor_names = [
            "Silicon", "Germanium", "GaAs", "InP", "GaN", "SiC", "AlN", "InAs",
            "GaP", "AlAs", "InSb", "CdTe", "ZnSe", "CuInSe2", "CIGS"
        ]
        
        crystal_systems = ["Diamond", "Zinc-blende", "Wurtzite", "Rock-salt", "Fluorite"]
        semiconductor_types = ["Elemental", "III-V", "II-VI", "IV-IV", "Ternary", "Quaternary"]
        
        data = []
        for i in range(n_materials):
            material = {
                "material_name": np.random.choice(semiconductor_names) + f"-{i%5}",
                "band_gap": np.random.uniform(0.1, 6.0),
                "electron_mobility": np.random.uniform(10, 8000),
                "hole_mobility": np.random.uniform(5, 2000),
                "dielectric_constant": np.random.uniform(3, 16),
                "refractive_index": np.random.uniform(1.5, 4.0),
                "lattice_constant": np.random.uniform(4.0, 7.0),
                "effective_mass_electron": np.random.uniform(0.05, 2.0),
                "effective_mass_hole": np.random.uniform(0.1, 3.0),
                "breakdown_field": np.random.uniform(0.1, 30),
                "thermal_conductivity": np.random.uniform(0.5, 500),
                "crystal_system": np.random.choice(crystal_systems),
                "semiconductor_type": np.random.choice(semiconductor_types),
                "dopant_concentration": np.random.uniform(1e14, 1e20)
            }
            data.append(material)
        
        self._dataset = pd.DataFrame(data)
    
    def calculate_intrinsic_carrier_concentration(self, temperature: float = 300) -> pd.Series:
        """Calculate intrinsic carrier concentration at given temperature."""
        # Simplified calculation using band gap
        kb = 8.617e-5  # Boltzmann constant in eV/K
        return 1e16 * np.exp(-self._dataset['band_gap'] / (2 * kb * temperature))
