# Features

Features are high-level workflows that combine multiple Information Units to solve specific materials science and electronics problems. Each feature implements a standardized processing pipeline while providing specialized functionality for different research domains.

## Overview

EMOS includes 16 features organized into two main categories:

### Materials Exploration Features (Features 1-8)
Advanced computational tools for materials discovery, characterization, and analysis:

- **Material Search** (ID: 1): Search across multiple materials databases
- **Material Generation** (ID: 2): Generate novel materials using AI models
- **Database Extractor** (ID: 3): Extract specific datasets from materials databases
- **Material Characterization** (ID: 4): Comprehensive material property analysis
- **DFT Calculation** (ID: 5): Quantum mechanical calculations using DFT
- **Crystallographic Analysis** (ID: 6): Crystal structure analysis and optimization
- **Quantum Mechanics** (ID: 7): Advanced quantum mechanical simulations
- **Tensor Analysis** (ID: 8): Materials tensor property calculations

[**→ View Detailed Materials Exploration Documentation**](materials_exploration.md)

### Electronics Application Features (Features 9-16)
Specialized tools for electronic device development, optimization, and analysis:

- **Device Synthesizability** (ID: 9): Assess device manufacturing feasibility
- **Interface Calculation** (ID: 10): Calculate interface properties and band alignments
- **Property Prediction** (ID: 11): Predict electronic and material properties using ML
- **Band Structure** (ID: 12): Electronic band structure calculations and analysis
- **Thermal Management** (ID: 13): Analyze thermal properties and heat dissipation
- **Reliability Assessment** (ID: 14): Device reliability analysis and lifetime prediction
- **Process Integration** (ID: 15): Manufacturing process optimization
- **Advanced Characterization** (ID: 16): Advanced electronic and structural characterization

[**→ View Detailed Electronics Application Documentation**](electronics_application.md)

Each feature follows a consistent workflow pattern:
1. **Input Extraction**: Parse and validate user inputs
2. **Information Unit Processing**: Activate selected databases, generators, and predictors
3. **Feature-Specific Processing**: Execute domain-specific algorithms
4. **Output Formatting**: Structure results for presentation

## Feature Architecture

### Base Feature Interface

All features inherit from `BaseFeature` and implement four key methods:

```python
class BaseFeature(ABC):
    @abstractmethod
    def info(self) -> str:
        """Return feature description"""
        pass
    
    @abstractmethod  
    def extract_inputs(self, input_data: dict) -> dict:
        """Extract and validate inputs from input_data"""
        pass
    
    @abstractmethod
    def process_feature(self, inputs: dict) -> dict:
        """Core feature processing logic"""
        pass
    
    @abstractmethod
    def format_outputs(self, results: dict) -> dict:
        """Format results to expected output format"""
        pass
```

### Template Method Pattern

Features follow a standard template method pattern:

```python
def process(self, input_data: dict) -> dict:
    """Main process method - template pattern"""
    # Step 1: Extract inputs
    inputs = self.extract_inputs(input_data)
    
    # Step 2: Process feature
    results = self.process_feature(inputs)
    
    # Step 3: Format outputs
    outputs = self.format_outputs(results)
    
    return outputs
```

### Information Unit Integration

All features can utilize any combination of Information Units:

```python
def _process_information_units(self, inputs):
    """Standard pattern for processing Information Units"""
    
    # Process databases
    for db_config in inputs.get('active_databases', []):
        db_instance = database_factory[db_config['value']](
            db_config['value'], self.logger
        )
        db_results = db_instance.retrieve(retrieve_inputs)
    
    # Process generators
    for gen_config in inputs.get('active_generators', []):
        gen_instance = generator_factory[gen_config['value']](
            gen_config['value'], self.logger
        )
        gen_results = gen_instance.generate(generate_inputs)
    
    # Process predictors
    for pred_config in inputs.get('active_predictors', []):
        pred_instance = predictor_factory[pred_config['value']](
            pred_config['value'], self.logger
        )
        pred_results = pred_instance.predict(predict_inputs)
```

## Feature Categories

### Materials Exploration Features

These features focus on fundamental materials research:

1. **Material Search** (ID: 1): Database querying and filtering
2. **Material Generation** (ID: 2): AI-powered material creation
3. **Database Extractor** (ID: 3): Bulk data extraction and analysis
4. **Material Characterization** (ID: 4): Property analysis and characterization
5. **DFT Calculation** (ID: 5): Density functional theory calculations
6. **Crystallographic Analysis** (ID: 6): Crystal structure analysis
7. **Quantum Mechanics** (ID: 7): Quantum mechanical property calculations
8. **Tensor Analysis** (ID: 8): Tensor property calculations and analysis

### Electronics Application Features

These features target electronic device applications:

1. **Device Synthesizability** (ID: 9): Manufacturing feasibility assessment
2. **Interface Calculation** (ID: 10): Interface properties and band alignments
3. **Property Prediction** (ID: 11): Electronic and material property prediction
4. **Band Structure** (ID: 12): Electronic band structure calculations
5. **Thermal Management** (ID: 13): Thermal property analysis and optimization
6. **Reliability Assessment** (ID: 14): Device reliability and lifetime prediction
7. **Process Integration** (ID: 15): Manufacturing process optimization
8. **Advanced Characterization** (ID: 16): Advanced electronic characterization

## Common Input Parameters

### Universal Parameters
All features accept these standard parameters:

- **active_databases**: List of database configurations to use
- **active_generators**: List of generator configurations to use
- **active_predictors**: List of predictor configurations to use

Example configuration:
```python
{
    'active_databases': [
        {'value': 'icsd', 'name': 'ICSD'},
        {'value': 'mp', 'name': 'Materials Project'}
    ],
    'active_generators': [
        {'value': 'mattergen', 'name': 'MatterGen'}
    ],
    'active_predictors': [
        {'value': 'm3gnet', 'name': 'M3GNet'},
        {'value': 'mattersim', 'name': 'MatterSim'}
    ]
}
```

### Feature-Specific Parameters
Each feature defines its own specific input parameters based on its functionality.

## Common Output Format

### Standard Output Structure
All features return structured results with:

```python
{
    'primary_results': {
        # Main computational outputs
    },
    'information_unit_results': {
        'databases': {...},
        'generators': {...},
        'predictors': {...}
    },
    'metadata': {
        'processing_time': float,
        'parameters_used': dict,
        'status': str
    },
    'warnings': [...],
    'errors': [...]
}
```

### Result Types

**Database Results**:
- Material identifiers and references
- Crystal structure data
- Experimental and computed properties

**Generator Results**:
- New material structures
- Generation confidence scores
- Novelty assessments

**Predictor Results**:
- Property predictions with uncertainty
- Confidence intervals
- Model performance metrics

## Usage Examples

### Basic Feature Usage

```python
from Features.FeatureFactory import create_feature

# Create feature instance
feature = create_feature("10", logger)  # Interface Calculation

# Prepare input data
input_data = {
    'interfaceType': 'metal-semiconductor',
    'materialA': 'Al',
    'materialB': 'Si',
    'calculationMethod': 'DFT',
    'active_databases': [{'value': 'icsd', 'name': 'ICSD'}],
    'active_predictors': [{'value': 'm3gnet', 'name': 'M3GNet'}]
}

# Process the feature
results = feature.process(input_data)
```

### Multi-Feature Workflow

```python
# Combine multiple features for comprehensive analysis
search_feature = create_feature("1", logger)  # Material Search
generation_feature = create_feature("2", logger)  # Material Generation
prediction_feature = create_feature("11", logger)  # Property Prediction

# Step 1: Search for similar materials
search_results = search_feature.process(search_inputs)

# Step 2: Generate new candidates
generation_inputs = {
    'seed_materials': search_results['candidates'],
    'target_properties': target_props,
    'active_generators': [{'value': 'mattergen', 'name': 'MatterGen'}]
}
generation_results = generation_feature.process(generation_inputs)

# Step 3: Predict properties of generated materials
prediction_inputs = {
    'materials': generation_results['generated_materials'],
    'properties': ['band_gap', 'formation_energy'],
    'active_predictors': [{'value': 'm3gnet', 'name': 'M3GNet'}]
}
final_results = prediction_feature.process(prediction_inputs)
```

## Error Handling and Logging

### Standard Error Handling
All features implement consistent error handling:

```python
def process_feature(self, inputs):
    try:
        if self.logger:
            self.logger.log('Starting feature processing...', 'info')
        
        # Main processing logic
        results = self._perform_calculations(inputs)
        
        if self.logger:
            self.logger.log('Feature processing completed successfully', 'info')
        
        return results
        
    except Exception as e:
        if self.logger:
            self.logger.log(f'Feature processing failed: {str(e)}', 'error')
        raise
```

### Information Unit Error Handling
```python
try:
    db_instance.retrieve(retrieve_inputs)
except Exception as e:
    if self.logger:
        self.logger.log(f'Database {db_key} retrieve() error: {str(e)}', 'warning')
    # Continue processing with other information units
```

## Adding New Features

The modular design makes it easy to add new features:

1. **Implement BaseFeature**: Create new feature class
2. **Register in Factory**: Add to `feature_factory` dictionary
3. **Follow Patterns**: Use standard information unit processing
4. **Document Interface**: Specify inputs, outputs, and behavior

Example of adding a new feature:

```python
class NewFeature(BaseFeature):
    def __init__(self, logger=None):
        super().__init__("New Feature", logger)
    
    def info(self):
        return "New Feature: Description of capabilities"
    
    def extract_inputs(self, input_data):
        return {
            'parameter1': input_data.get('param1', 'default'),
            'active_databases': input_data.get('active_databases', []),
            'active_generators': input_data.get('active_generators', []),
            'active_predictors': input_data.get('active_predictors', [])
        }
    
    def process_feature(self, inputs):
        # Process information units
        self._process_information_units(inputs)
        
        # Feature-specific logic
        results = self._custom_processing(inputs)
        
        return results
    
    def format_outputs(self, results):
        return {
            'result1': results.get('output1', 'N/A'),
            'result2': results.get('output2', 'N/A')
        }

# Register in factory
feature_factory["17"] = NewFeature
```

This modular approach ensures that EMOS can easily grow with new research capabilities while maintaining consistency and reliability.