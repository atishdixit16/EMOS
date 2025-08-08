// Interface Calculation Feature
class InterfaceCalculationFeature extends BaseFeature {
    constructor() {
        super(10, 'Interface Calculation', 'Calculate and analyze interfaces between different materials in electronic applications');
    }

    createInputsHTML() {
        return `
            <p>Configure interface calculation parameters</p>
            <div class="input-controls">
                ${this.createTextInput(`material1_${this.featureId}`, 'Material 1', 'e.g., Si, GaAs, AlN', true)}
                ${this.createTextInput(`material2_${this.featureId}`, 'Material 2', 'e.g., SiO2, Al2O3, HfO2', true)}
                ${this.createSelectInput(`interfaceType_${this.featureId}`, 'Interface Type', [
                    { value: 'coherent', text: 'Coherent Interface' },
                    { value: 'semicoherent', text: 'Semi-coherent Interface' },
                    { value: 'incoherent', text: 'Incoherent Interface' },
                    { value: 'grain_boundary', text: 'Grain Boundary' }
                ])}
                ${this.createSelectInput(`calculationMethod_${this.featureId}`, 'Calculation Method', [
                    { value: 'dft', text: 'DFT (First Principles)' },
                    { value: 'classical_md', text: 'Classical Molecular Dynamics' },
                    { value: 'tight_binding', text: 'Tight Binding' },
                    { value: 'empirical', text: 'Empirical Models' }
                ])}
                ${this.createNumberInput(`supercellSize_${this.featureId}`, 'Supercell Size (atoms)', '50', '1000', '10')}
                ${this.createCheckboxInput(`includeStrain_${this.featureId}`, 'Include Strain Effects', true)}
                ${this.createCheckboxInput(`calculateBandOffset_${this.featureId}`, 'Calculate Band Offset', true)}
            </div>
        `;
    }

    createOutputsHTML() {
        return `
            <p>Interface calculation results and properties</p>
            <div class="output-display" id="outputDisplay_${this.featureId}">
                <div class="output-item">
                    <strong>Interface Energy:</strong> <span id="interfaceEnergy_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Band Offset:</strong> <span id="bandOffset_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Lattice Mismatch:</strong> <span id="latticeMismatch_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Interface States:</strong> <span id="interfaceStates_${this.featureId}">Pending...</span>
                </div>
                <div class="output-item">
                    <strong>Charge Transfer:</strong> <span id="chargeTransfer_${this.featureId}">Pending...</span>
                </div>
            </div>
        `;
    }

    async processFeature() {
        const material1 = this.getInputValue(`material1_${this.featureId}`);
        const material2 = this.getInputValue(`material2_${this.featureId}`);
        const interfaceType = this.getInputValue(`interfaceType_${this.featureId}`);
        const includeStrain = this.getInputValue(`includeStrain_${this.featureId}`);
        const calculateBandOffset = this.getInputValue(`calculateBandOffset_${this.featureId}`);
        
        // Simulate interface calculations
        const interfaceEnergy = (Math.random() * 2 + 0.5).toFixed(3); // 0.5-2.5 J/m²
        const bandOffset = calculateBandOffset ? (Math.random() * 3 + 0.2).toFixed(2) : 'Not calculated';
        const latticeMismatch = (Math.random() * 5 + 0.1).toFixed(2); // 0.1-5.1%
        const interfaceStates = Math.floor(Math.random() * 5e12) + 1e12; // states/cm²
        const chargeTransfer = (Math.random() * 0.5 + 0.1).toFixed(3); // electrons
        
        return {
            interfaceEnergy: `${interfaceEnergy} J/m²`,
            bandOffset: calculateBandOffset ? `${bandOffset} eV` : 'Not calculated',
            latticeMismatch: `${latticeMismatch}%`,
            interfaceStates: `${interfaceStates.toExponential(2)} states/cm²`,
            chargeTransfer: `${chargeTransfer} e⁻`
        };
    }

    updateOutputs(results = null) {
        const finalResults = results || this.results;
        
        document.getElementById(`interfaceEnergy_${this.featureId}`).textContent = finalResults.interfaceEnergy;
        document.getElementById(`bandOffset_${this.featureId}`).textContent = finalResults.bandOffset;
        document.getElementById(`latticeMismatch_${this.featureId}`).textContent = finalResults.latticeMismatch;
        document.getElementById(`interfaceStates_${this.featureId}`).textContent = finalResults.interfaceStates;
        document.getElementById(`chargeTransfer_${this.featureId}`).textContent = finalResults.chargeTransfer;
    }
}

window.InterfaceCalculationFeature = InterfaceCalculationFeature;
