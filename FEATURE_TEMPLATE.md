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
            <p>Configure [feature specific] parameters</p>
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
                    <strong>Output 1 Label:</strong> <span id="semanticOutput1_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Output 2 Label:</strong> <span id="semanticOutput2_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Output 3 Label:</strong> <span id="semanticOutput3_${this.featureId}">Pending...</span>
                </div>
            </div>
        `;
    }

    async processFeature() {
        // Simple fixed results for [feature name] - JavaScript fallback
        return {
            semanticOutput1: '[Fixed descriptive result 1]',
            semanticOutput2: '[Fixed descriptive result 2]',
            semanticOutput3: '[Fixed descriptive result 3]'
        };
    }

    updateOutputs(results = null) {
        const finalResults = results || this.results;
        
        document.getElementById(`semanticOutput1_${this.featureId}`).textContent = finalResults.semanticOutput1;
        document.getElementById(`semanticOutput2_${this.featureId}`).textContent = finalResults.semanticOutput2;
        document.getElementById(`semanticOutput3_${this.featureId}`).textContent = finalResults.semanticOutput3;
    }
}

window.[FeatureName]Feature = [FeatureName]Feature;
```

## Python Backend Template

Each feature also requires a corresponding `processor.py` file for Python backend processing:

```python
# Features/[Category]/[Feature_Name]/processor.py
def process(input_data):
    """
    Process [feature name] with user inputs
    Args:
        input_data (dict): User input values from the form
    Returns:
        dict: Results matching the feature's expected output format
    """
    # Extract inputs with defaults
    param1 = input_data.get('param1', 'default_value')
    param2 = input_data.get('param2', 'default_value')
    param3 = input_data.get('param3', 'default_value')
    param4 = input_data.get('param4', False)
    
    # Processing logic based on inputs
    # ... (implement actual calculations here) ...
    
    # Return results matching [FeatureName].js output format with 'python' string
    return {
        'semanticOutput1': '[Calculated result 1] - python',
        'semanticOutput2': '[Calculated result 2] - python',
        'semanticOutput3': '[Calculated result 3] - python'
    }
```

## Backend Processing Architecture

### **Flow Diagram:**
```
UI Input → BaseFeature.collectInputData() → HTTP POST → processor.py → Results → UI Output
    ↓ (if backend fails)
JavaScript fallback → processFeature() → Local Results → UI Output
```

### **BaseFeature Backend Integration:**
The BaseFeature class automatically handles:
1. **Input Collection**: `collectInputData()` gathers all form inputs
2. **Backend API Call**: `callPythonBackend()` sends POST request to Flask server
3. **Fallback Mechanism**: Falls back to JavaScript `processFeature()` if backend fails
4. **Result Display**: `updateOutputs()` shows results with "- python" suffix when backend succeeds

### **Flask Server Configuration:**
- **Endpoint Pattern**: `/api/process/{featureId}`
- **Server Port**: 5001
- **CORS Enabled**: For cross-origin requests from frontend
- **Auto-Discovery**: Dynamically loads processor.py files for each feature

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
All features MUST have exactly these 4 methods:
- `createInputsHTML()` - Define input controls
- `createOutputsHTML()` - Define output display structure  
- `processFeature()` - JavaScript fallback processing
- `updateOutputs()` - Update UI with results

### 5. **Input Controls**
Use BaseFeature helper methods:
- `this.createSelectInput()` for dropdowns
- `this.createNumberInput()` for numeric inputs
- `this.createTextInput()` for text fields
- `this.createCheckboxInput()` for checkboxes
- `this.createFileInput()` for file uploads

### 6. **Output Structure**
- Use semantic output IDs (not generic `result1/result2/result3`)
- Each output in a `<div class="output-item">` 
- Use `<strong>` for labels and `<span>` for values
- Initialize all with "Pending..."
- **CRITICAL**: Output IDs must match Python processor.py return keys

### 7. **Processing Logic**
- **Primary**: Python backend processing via `processor.py`
- **Fallback**: JavaScript `processFeature()` for offline/backend-failure scenarios
- Return object with descriptive property names
- **MUST** match property names between JS and Python

### 8. **Python Backend Integration**
- Each feature requires a `processor.py` file in its directory
- Python results include "- python" suffix for identification
- Automatic fallback to JavaScript if backend unavailable
- Input data automatically collected and sent to Python backend

### 9. **Window Export**
- Always end with `window.[FeatureName]Feature = [FeatureName]Feature;`

## Backend Server Configuration

### **Flask Server Setup:**
```bash
# Install dependencies
conda install flask flask-cors

# Start server
cd /home/soe/EMOS/backend
python app.py

# Server runs on http://localhost:5001
# Endpoints: /api/process/1 through /api/process/16
```

### **Feature ID Mapping:**
```javascript
1: Material Search          9: Device Synthesizability
2: Material Generation      10: Interface Calculation  
3: Database Extractor       11: Property Prediction
4: Material Characterization 12: Band Structure
5: DFT Calculation          13: Thermal Management
6: Crystallographic Analysis 14: Reliability Assessment
7: Quantum Mechanics        15: Process Integration
8: Tensor Analysis          16: Advanced Characterization
```

## Features Updated to Standard Template:

✅ **ALL 16 FEATURES FULLY IMPLEMENTED:**

### **Materials Exploration (8 features):**
1. **Material Search** - Search and filter materials from databases
2. **Material Generation** - AI-powered generation of new material compositions  
3. **Database Extractor** - Extract and analyze material properties from databases
4. **Material Characterization** - Analyze material properties and structure
5. **DFT Calculation** - Density Functional Theory calculations
6. **Crystallographic Analysis** - Crystal structure analysis and modeling
7. **Quantum Mechanics** - Quantum mechanical property calculations
8. **Tensor Analysis** - Tensor property analysis and correlations

### **Electronics Application (8 features):**
9. **Device Synthesizability** - Evaluate device fabrication feasibility
10. **Interface Calculation** - Calculate material interface properties
11. **Property Prediction** - Predict electronic and material properties
12. **Band Structure** - Calculate and analyze electronic band structures
13. **Thermal Management** - Optimize thermal management solutions
14. **Reliability Assessment** - Assess device reliability and failure modes
15. **Process Integration** - Integrate and optimize fabrication processes
16. **Advanced Characterization** - Advanced material characterization techniques

## Implementation Status:

🎯 **ALL FEATURES NOW INCLUDE:**
- ✅ Standardized JavaScript templates with exactly 4 methods each
- ✅ Semantic output names (no generic result1/result2/result3)  
- ✅ Python backend integration via `processor.py` files
- ✅ Automatic fallback to JavaScript when backend unavailable
- ✅ Fixed return values for consistent testing and development
- ✅ Matching output keys between JavaScript and Python implementations

## Backend Integration Features:

### **Automatic Processing Flow:**
1. **User clicks "Start Processing"** → BaseFeature.startProcessing()
2. **Collect inputs** → BaseFeature.collectInputData()
3. **Try Python backend** → HTTP POST to /api/process/{featureId}
4. **If successful** → Display results with "- python" suffix
5. **If backend fails** → Fallback to JavaScript processFeature()
6. **Update UI** → updateOutputs() displays final results

### **Development Workflow:**
1. **Frontend Development**: Modify JavaScript files for UI changes
2. **Backend Development**: Modify processor.py files for computation logic
3. **Testing**: Start Flask server and test via UI
4. **Debugging**: Check browser console and Flask terminal for errors

**Note: All features use simplified fixed return values instead of complex calculations for easier testing and development. The Python backend architecture allows for easy implementation of actual computational logic in the processor.py files.**

This template ensures consistency, maintainability, and proper integration with the BaseFeature class and Python backend processing system.

## Quick Start Guide:

### **To Run EMOS with Python Backend:**
```bash
# 1. Start Python backend
cd /home/soe/EMOS/backend
conda activate emos  # or your conda environment
python app.py

# 2. Start frontend (new terminal)
cd /home/soe/EMOS
python -m http.server 8000

# 3. Open browser
http://localhost:8000
```

### **To Add a New Feature:**
1. Create feature JavaScript file following the template
2. Create corresponding `processor.py` file
3. Add feature mapping to Flask server `app.py`
4. Add feature button to frontend HTML
5. Test both Python backend and JavaScript fallback

### **To Modify Existing Feature:**
1. **UI Changes**: Edit the JavaScript file
2. **Processing Logic**: Edit the `processor.py` file  
3. **Ensure Output Keys Match**: JavaScript updateOutputs() IDs must match Python return keys
4. Restart Flask server to see Python changes

The EMOS system now provides a robust, scalable architecture for materials science feature development with automatic backend integration and fallback mechanisms.
