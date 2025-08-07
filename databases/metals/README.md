# Metals and Alloys Database

## Overview
The Metals Database is a comprehensive collection of metallic materials including pure metals, alloys, and intermetallic compounds. This database focuses on mechanical, thermal, electrical, and magnetic properties essential for engineering applications.

## Database Properties

### Available Properties and Units

| Property | Unit | Description |
|----------|------|-------------|
| material_name | string | Unique identifier for the material |
| density | g/cm³ | Mass density of the material |
| melting_point | °C | Temperature at which material melts |
| thermal_conductivity | W/m·K | Heat conduction capability |
| electrical_resistivity | µΩ·cm | Electrical resistance property |
| young_modulus | GPa | Elastic modulus (stiffness) |
| yield_strength | MPa | Stress at which plastic deformation begins |
| ultimate_tensile_strength | MPa | Maximum stress before failure |
| hardness_hv | HV | Vickers hardness measurement |
| thermal_expansion | 10⁻⁶/K | Linear thermal expansion coefficient |
| poisson_ratio | dimensionless | Ratio of lateral to axial strain |
| crystal_structure | string | Crystallographic structure type |
| magnetic_property | string | Magnetic behavior classification |

## Usage Examples

### Basic Property Query
```python
from databases.metals import MetalsDatabase

# Initialize database
metals_db = MetalsDatabase()

# Get available properties
properties = metals_db.get_available_properties()
print(properties)

# Query high-strength materials
high_strength = metals_db.query_materials({
    'yield_strength': 800  # Materials with ~800 MPa yield strength
}, max_count=10)
```

### Advanced Filtering
```python
# Find materials suitable for high-temperature applications
heat_resistant = metals_db.query_materials({
    'melting_point': 1500,  # High melting point
    'thermal_conductivity': 50  # Good thermal conductivity
}, max_count=20)

# Get alloy composition
composition = metals_db.get_alloy_composition("Steel-304-Variant1")
```

## Special Features

### Alloy Composition Analysis
The metals database includes a special method to retrieve detailed alloy compositions:
- `get_alloy_composition(material_name)`: Returns elemental composition percentages

### Property Ranges
- **Density**: 2.5 - 19.3 g/cm³ (from Magnesium to Gold-based alloys)
- **Melting Point**: 300 - 3400°C (from low-melting alloys to Tungsten)
- **Yield Strength**: 50 - 1500 MPa (from soft metals to superalloys)

## Applications
- Structural engineering
- Aerospace components
- Automotive parts
- Electronic packaging
- Heat exchangers
- Magnetic components

## Data Quality
- 150 materials in database
- Properties validated against metallurgical standards
- Regular updates with new alloy developments
- Cross-referenced with industry databases
