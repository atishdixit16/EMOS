// Base Feature Class - Foundation for all EMOS features
class BaseFeature {
    constructor(featureId, featureName, featureDescription) {
        this.featureId = featureId;
        this.featureName = featureName;
        this.featureDescription = featureDescription;
        this.isProcessing = false;
        this.results = null;
    }

    // Create the complete feature interface
    createFeatureHTML() {
        return `
            <div class="feature-header">
                <div class="feature-title-section">
                    <h3><span id="featureTitle">${this.featureName}</span> Processing</h3>
                    <p class="feature-subtitle" id="featureSubtitle">${this.featureDescription}</p>
                </div>
                <button class="close-feature" id="closeFeature">×</button>
            </div>
            
            <div class="process-section">
                <h3>Inputs</h3>
                <div class="process-content" id="inputsContent">
                    ${this.createInputsHTML()}
                </div>
            </div>
            
            <div class="process-section">
                <h3>Processing</h3>
                <div class="process-content" id="processingContent">
                    ${this.createProcessingHTML()}
                </div>
            </div>
            
            <div class="process-section">
                <h3>Outputs</h3>
                <div class="process-content" id="outputsContent">
                    ${this.createOutputsHTML()}
                </div>
            </div>
        `;
    }

    // Override in subclasses for specific inputs
    createInputsHTML() {
        return `
            <p>Configure your input parameters for ${this.featureName}</p>
            <div class="input-controls">
                <label>Parameter 1: <input type="text" placeholder="Enter value" id="param1_${this.featureId}"></label>
                <label>Parameter 2: <input type="text" placeholder="Enter value" id="param2_${this.featureId}"></label>
                <label>Parameter 3: <input type="text" placeholder="Enter value" id="param3_${this.featureId}"></label>
            </div>
        `;
    }

    // Override in subclasses for specific processing UI
    createProcessingHTML() {
        return `
            <p>Processing ${this.featureName}...</p>
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill_${this.featureId}"></div>
            </div>
            <button class="process-btn" id="processBtn_${this.featureId}" onclick="window.features[${this.featureId}].startProcessing()">Start Processing</button>
        `;
    }

    // Override in subclasses for specific outputs
    createOutputsHTML() {
        return `
            <p>Results for ${this.featureName}</p>
            <div class="output-display" id="outputDisplay_${this.featureId}">
                <div class="output-item">
                    <strong>Result 1:</strong> <span id="result1_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Result 2:</strong> <span id="result2_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Result 3:</strong> <span id="result3_${this.featureId}">Pending...</span>
                </div>
            </div>
        `;
    }

    // Utility methods for creating different input types
    createTextInput(id, label, placeholder = '', required = false) {
        const req = required ? 'required' : '';
        return `
            <label>${label}: 
                <input type="text" id="${id}" placeholder="${placeholder}" ${req}>
            </label>
        `;
    }

    createNumberInput(id, label, min = '', max = '', step = '1', required = false) {
        const req = required ? 'required' : '';
        return `
            <label>${label}: 
                <input type="number" id="${id}" min="${min}" max="${max}" step="${step}" ${req}>
            </label>
        `;
    }

    createSelectInput(id, label, options, required = false) {
        const req = required ? 'required' : '';
        const optionsHTML = options.map(opt => 
            `<option value="${opt.value}">${opt.text}</option>`
        ).join('');
        return `
            <label>${label}: 
                <select id="${id}" ${req}>
                    ${optionsHTML}
                </select>
            </label>
        `;
    }

    createFileInput(id, label, accept = '') {
        return `
            <label>${label}: 
                <input type="file" id="${id}" accept="${accept}">
            </label>
        `;
    }

    createCheckboxInput(id, label, checked = false) {
        const checkedAttr = checked ? 'checked' : '';
        return `
            <label>
                <input type="checkbox" id="${id}" ${checkedAttr}> ${label}
            </label>
        `;
    }

    // Processing methods
    async startProcessing() {
        if (this.isProcessing) return;
        
        this.isProcessing = true;
        const processBtn = document.getElementById(`processBtn_${this.featureId}`);
        const progressFill = document.getElementById(`progressFill_${this.featureId}`);
        
        if (processBtn) {
            processBtn.disabled = true;
            processBtn.textContent = 'Processing...';
        }
        
        if (progressFill) {
            progressFill.style.width = '0%';
            progressFill.style.width = '100%';
        }
        
        try {
            // Try Python backend first
            console.log(`Calling Python backend for feature ${this.featureId}`);
            const results = await this.callPythonBackend();
            this.results = results;
            this.updateOutputs();
        } catch (error) {
            console.log('Backend failed, using local processing:', error);
            // Simulate processing time
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            // Fallback to local processFeature
            this.results = await this.processFeature();
            this.updateOutputs();
        }
        
        try {
            console.error('Processing error:', error);
            this.updateOutputs({ error: error.message });
        } finally {
            this.isProcessing = false;
            if (processBtn) {
                processBtn.disabled = false;
                processBtn.textContent = 'Start Processing';
            }
            if (progressFill) {
                setTimeout(() => {
                    progressFill.style.width = '0%';
                }, 1000);
            }
        }
    }

    // Simulate processing for features that don't have complex processing
    async simulateProcessing() {
        return new Promise(resolve => setTimeout(resolve, 1500));
    }

    // Override in subclasses for specific processing logic
    async processFeature() {
        return {
            result1: 'Processing complete',
            result2: 'Analysis finished',
            result3: 'Results generated'
        };
    }

    // Override in subclasses for specific output updates
    updateOutputs(results = null) {
        const finalResults = results || this.results;
        
        if (finalResults.error) {
            document.getElementById(`result1_${this.featureId}`).textContent = `Error: ${finalResults.error}`;
            return;
        }
        
        if (finalResults.result1) {
            document.getElementById(`result1_${this.featureId}`).textContent = finalResults.result1;
        }
        if (finalResults.result2) {
            document.getElementById(`result2_${this.featureId}`).textContent = finalResults.result2;
        }
        if (finalResults.result3) {
            document.getElementById(`result3_${this.featureId}`).textContent = finalResults.result3;
        }
    }

    // Utility method to get input values
    getInputValue(id) {
        const element = document.getElementById(id);
        if (!element) return null;
        
        if (element.type === 'checkbox') {
            return element.checked;
        }
        return element.value;
    }

    async callPythonBackend() {
        // Collect input data for this feature
        const inputs = this.collectInputData();
        
        // Call Python backend
        const response = await fetch(`http://localhost:5001/api/process/${this.featureId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(inputs)
        });
        
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return await response.json();
    }

    collectInputData() {
        // Collect all input values for this feature
        const inputs = {};
        const inputElements = document.querySelectorAll(`[id$="_${this.featureId}"]`);
        
        inputElements.forEach(element => {
            const key = element.id.replace(`_${this.featureId}`, '');
            if (element.type === 'checkbox') {
                inputs[key] = element.checked;
            } else {
                inputs[key] = element.value;
            }
        });
        
        return inputs;
    }
}

// Export for use in other files
if (typeof window !== 'undefined') {
    window.BaseFeature = BaseFeature;
}
