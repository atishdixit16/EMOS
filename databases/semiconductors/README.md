# Semiconductors Database

## Overview
The Semiconductors Database contains electronic and optical properties of semiconductor materials including elemental semiconductors, III-V compounds, II-VI compounds, and advanced semiconductor alloys used in electronic devices.

## Database Properties

### Available Properties and Units

| Property | Unit | Description |
|----------|------|-------------|
| material_name | string | Semiconductor material identifier |
| band_gap | eV | Energy gap between valence and conduction bands |
| electron_mobility | cm²/V·s | Electron mobility at room temperature |
| hole_mobility | cm²/V·s | Hole mobility at room temperature |
| dielectric_constant | dimensionless | Relative permittivity |
| refractive_index | dimensionless | Optical refractive index |
| lattice_constant | Å | Crystal lattice parameter |
| effective_mass_electron | m₀ | Effective mass of electrons |
| effective_mass_hole | m₀ | Effective mass of holes |
| breakdown_field | MV/cm | Electric field at breakdown |
| thermal_conductivity | W/m·K | Heat conduction capability |
| crystal_system | string | Crystal structure classification |
| semiconductor_type | string | Material type classification |
| dopant_concentration | cm⁻³ | Carrier concentration |

## Usage Examples

### Electronic Device Design
```python
from databases.semiconductors import SemiconductorsDatabase

# Initialize database
semi_db = SemiconductorsDatabase()

# Find wide bandgap semiconductors for power electronics
wide_bandgap = semi_db.query_materials({
    'band_gap': 3.0,  # > 3 eV bandgap
    'breakdown_field': 1.0  # High breakdown field
}, max_count=15)

# Calculate intrinsic carrier concentration
ni = semi_db.calculate_intrinsic_carrier_concentration(temperature=300)
```

### Optical Applications
```python
# Find materials for optical devices
optical_materials = semi_db.query_materials({
    'refractive_index': 3.5,  # High refractive index
    'band_gap': 1.5  # Suitable for infrared applications
})
```

## Special Features

### Intrinsic Carrier Calculation
- `calculate_intrinsic_carrier_concentration(temperature)`: Computes carrier concentration at specified temperature
- Uses band gap and temperature to estimate intrinsic properties

### Material Classifications
- **Elemental**: Si, Ge
- **III-V**: GaAs, InP, GaN, AlN
- **II-VI**: CdTe, ZnSe
- **Ternary/Quaternary**: Complex alloys

### Property Ranges
- **Band Gap**: 0.1 - 6.0 eV (from narrow gap to wide gap)
- **Electron Mobility**: 10 - 8000 cm²/V·s
- **Dielectric Constant**: 3 - 16

## Applications
- Solar cells and photovoltaics
- Light-emitting diodes (LEDs)
- Laser diodes
- Power electronics
- Radio frequency devices
- Photodetectors

## Data Quality
- 120 semiconductor materials
- Temperature-dependent properties available
- Band structure calculations included
- Updated with latest III-V and wide bandgap materials
