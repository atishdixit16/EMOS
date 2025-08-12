# EMOS Feature Code Template

## Standard Template for All Feature .js Files

All EMOS feature JavaScript files should follow this exact template and coding style:

```javascript
// [Feature Name] Feature
class [FeatureName]Feature extends BaseFeature {
    constructor() {
        super([featureId], '[Feature Display Name]', '[Feature description for UI]');
    }

    createInputsHTML() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createSelectInput(`param1_${this.featureId}`, 'Parameter 1 Label', [
                    { value: 'option1', text: 'Option 1' },
                    { value: 'option2', text: 'Option 2' }
                ])}
                ${this.createNumberInput(`param2_${this.featureId}`, 'Parameter 2 Label', 'min', 'max', 'step')}
                ${this.createTextInput(`param3_${this.featureId}`, 'Parameter 3 Label', 'placeholder text')}
                ${this.createCheckboxInput(`param4_${this.featureId}`, 'Parameter 4 Label', true)}
            </div>
        `;
    }

    createOutputsHTML() {
        return `
            <p>[Feature name] results and [specific type] information</p>
            <div class="output-display" id="outputDisplay_${this.featureId}">
                <div class="output-item">
                    <strong>Output 1 Label:</strong> <span id="output1_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Output 2 Label:</strong> <span id="output2_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Output 3 Label:</strong> <span id="output3_${this.featureId}">Pending...</span>
                </div>
            </div>
        `;
    }

    async processFeature() {
        // Simple fixed results for [feature name]
        return {
            output1: '[Fixed descriptive result 1]',
            output2: '[Fixed descriptive result 2]',
            output3: '[Fixed descriptive result 3]'
        };
    }

    updateOutputs(results = null) {
        const finalResults = results || this.results;
        
        document.getElementById(`output1_${this.featureId}`).textContent = finalResults.output1;
        document.getElementById(`output2_${this.featureId}`).textContent = finalResults.output2;
        document.getElementById(`output3_${this.featureId}`).textContent = finalResults.output3;
    }
}

window.[FeatureName]Feature = [FeatureName]Feature;
```

## Key Standards Applied:

### 1. **File Header Comment**
- Always start with `// [Feature Name] Feature`
- Use proper feature name (not abbreviated)

### 2. **Class Declaration** 
- Class name: `[FeatureName]Feature` (PascalCase)
- Always extends `BaseFeature`

### 3. **Constructor**
- Always call `super(featureId, featureName, description)`
- Use proper feature ID number from the mapping

### 4. **Required Methods**
All features MUST have these methods:
- `createInputsHTML()` - Define input controls
- `createOutputsHTML()` - Define output display structure  
- `processFeature()` - Core processing logic
- `updateOutputs()` - Update UI with results

### 5. **Input Controls**
Use BaseFeature helper methods:
- `this.createSelectInput()` for dropdowns
- `this.createNumberInput()` for numeric inputs
- `this.createTextInput()` for text fields
- `this.createCheckboxInput()` for checkboxes
- `this.createFileInput()` for file uploads

### 6. **Output Structure**
- Use semantic output IDs (not `result1/result2/result3`)
- Each output in a `<div class="output-item">` 
- Use `<strong>` for labels and `<span>` for values
- Initialize all with "Pending..."

### 7. **Processing Logic**
- Get inputs using `this.getInputValue()`
- Include realistic simulations/calculations
- Return object with descriptive property names
- Match property names with output element IDs

### 8. **Window Export**
- Always end with `window.[FeatureName]Feature = [FeatureName]Feature;`

## Features Updated to Standard Template:

✅ **Already Standardized:**
- Material Search (MaterialSearchFeature)
- Material Generation (MaterialGenerationFeature) 
- Database Extractor (DatabaseExtractorFeature)
- Device Synthesizability (DeviceSynthesizabilityFeature)
- Interface Calculation (InterfaceCalculationFeature)

✅ **Recently Standardized:**
- DFT Calculation (DFTCalculationFeature)
- Process Integration (ProcessIntegrationFeature)
- Band Structure (BandStructureFeature)
- Crystallographic Analysis (CrystallographicAnalysisFeature)
- Material Characterization (MaterialCharacterizationFeature)
- Quantum Mechanics (QuantumMechanicsFeature)
- Tensor Analysis (TensorAnalysisFeature)
- Property Prediction (PropertyPredictionFeature)
- Thermal Management (ThermalManagementFeature)
- Reliability Assessment (ReliabilityAssessmentFeature)
- Advanced Characterization (AdvancedCharacterizationFeature)

🎯 **ALL FEATURES NOW STANDARDIZED AND SIMPLIFIED!**

All 16 EMOS features now follow the consistent template with:
- Proper semantic output names (no more result1/result2/result3)
- Complete createOutputsHTML() and updateOutputs() methods
- **SIMPLIFIED: All processFeature() methods return fixed values**
- Consistent code structure and formatting

**Note: All features now use simple fixed return values instead of dynamic calculations for easier testing and development.**

This template ensures consistency, maintainability, and proper integration with the BaseFeature class and backend processing system.
