# Polymers and Composites Database

## Overview
The Polymers Database encompasses thermoplastics, thermosets, elastomers, and polymer composites. It focuses on mechanical, thermal, electrical, and processing properties essential for plastic part design and manufacturing.

## Database Properties

### Available Properties and Units

| Property | Unit | Description |
|----------|------|-------------|
| material_name | string | Polymer material identifier |
| density | g/cm³ | Bulk density of the polymer |
| glass_transition_temp | °C | Glass transition temperature |
| melting_point | °C | Melting/decomposition temperature |
| tensile_strength | MPa | Ultimate tensile strength |
| elongation_at_break | % | Strain at failure |
| flexural_modulus | GPa | Stiffness in bending |
| impact_strength | J/m | Energy absorption capacity |
| thermal_conductivity | W/m·K | Heat conduction capability |
| specific_heat | J/g·K | Heat capacity per unit mass |
| dielectric_strength | kV/mm | Electrical breakdown voltage |
| volume_resistivity | Ω·cm | Electrical resistance |
| water_absorption | % | Moisture uptake |
| mold_shrinkage | % | Dimensional change during molding |
| polymer_type | string | Polymer classification |
| crystallinity | % | Degree of crystalline order |
| molecular_weight | g/mol | Average molecular weight |

## Usage Examples

### Material Selection for Design
```python
from databases.polymers import PolymersDatabase

# Initialize database
polymers_db = PolymersDatabase()

# Find high-strength polymers
strong_polymers = polymers_db.query_materials({
    'tensile_strength': 100,  # > 100 MPa
    'flexural_modulus': 5     # > 5 GPa stiffness
}, max_count=15)

# Get processing conditions
processing = polymers_db.get_processing_conditions("PE-5")
print(processing)
```

### Electrical Applications
```python
# Find electrical insulation materials
insulators = polymers_db.query_materials({
    'dielectric_strength': 20,    # High breakdown voltage
    'volume_resistivity': 1e15    # High resistivity
})
```

## Special Features

### Processing Conditions Calculation
- `get_processing_conditions(material_name)`: Returns recommended:
  - Processing temperature range
  - Injection pressure
  - Cooling rate
  - Mold temperature

### Polymer Classifications
- **Thermoplastic**: PE, PP, PS, PVC, PET
- **Thermoset**: Epoxy, polyurethane, phenolic
- **Elastomer**: Rubber compounds
- **Composite**: Fiber-reinforced polymers
- **Biopolymer**: Biodegradable materials

### Property Ranges
- **Density**: 0.8 - 2.2 g/cm³
- **Tensile Strength**: 10 - 200 MPa
- **Glass Transition**: -100 to 200°C

## Applications
- Automotive components
- Electronic housings
- Packaging materials
- Medical devices
- Consumer products
- Aerospace interiors

## Processing Information
The database includes processing-related properties:
- Mold shrinkage for injection molding
- Glass transition for thermoforming
- Melting point for extrusion
- Water absorption for environmental stability

## Data Quality
- 80 polymer materials
- Processing conditions included
- Temperature-dependent properties
- Validated against polymer handbooks
- Regular updates with new bio-based materials
