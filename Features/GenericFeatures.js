// Generic Feature Class for Features 4-8 and 11-16
class GenericFeature extends BaseFeature {
    constructor(featureId, featureName, featureDescription) {
        super(featureId, featureName, featureDescription);
    }

    createInputsHTML() {
        // Vary the input types based on feature ID for some diversity
        const inputVariations = {
            4: this.createFeature4Inputs(),
            5: this.createFeature5Inputs(),
            6: this.createFeature6Inputs(),
            7: this.createFeature7Inputs(),
            8: this.createFeature8Inputs(),
            11: this.createFeature11Inputs(),
            12: this.createFeature12Inputs(),
            13: this.createFeature13Inputs(),
            14: this.createFeature14Inputs(),
            15: this.createFeature15Inputs(),
            16: this.createFeature16Inputs()
        };

        return inputVariations[this.featureId] || this.createDefaultInputs();
    }

    createFeature4Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createTextInput(`parameter1_${this.featureId}`, 'Material Formula', 'e.g., Al2O3, SiC')}
                ${this.createSelectInput(`analysisType_${this.featureId}`, 'Analysis Type', [
                    { value: 'basic', text: 'Basic Analysis' },
                    { value: 'advanced', text: 'Advanced Analysis' },
                    { value: 'comprehensive', text: 'Comprehensive Analysis' }
                ])}
                ${this.createNumberInput(`threshold_${this.featureId}`, 'Threshold Value', '0', '100', '0.1')}
                ${this.createCheckboxInput(`exportResults_${this.featureId}`, 'Export Results', true)}
            </div>
        `;
    }

    createFeature5Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createSelectInput(`optimizationTarget_${this.featureId}`, 'Optimization Target', [
                    { value: 'performance', text: 'Performance' },
                    { value: 'cost', text: 'Cost' },
                    { value: 'efficiency', text: 'Efficiency' }
                ])}
                ${this.createNumberInput(`iterations_${this.featureId}`, 'Iterations', '10', '1000', '10')}
                ${this.createFileInput(`configFile_${this.featureId}`, 'Configuration File', '.json,.xml')}
                ${this.createCheckboxInput(`verboseOutput_${this.featureId}`, 'Verbose Output', false)}
            </div>
        `;
    }

    createFeature6Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createTextInput(`inputData_${this.featureId}`, 'Input Data', 'Enter data or formula')}
                ${this.createSelectInput(`modelType_${this.featureId}`, 'Model Type', [
                    { value: 'linear', text: 'Linear Model' },
                    { value: 'nonlinear', text: 'Non-linear Model' },
                    { value: 'ml', text: 'Machine Learning' }
                ])}
                ${this.createNumberInput(`accuracy_${this.featureId}`, 'Required Accuracy (%)', '50', '99', '1')}
                ${this.createCheckboxInput(`realTimeUpdate_${this.featureId}`, 'Real-time Updates', true)}
            </div>
        `;
    }

    createFeature7Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createSelectInput(`computationMethod_${this.featureId}`, 'Computation Method', [
                    { value: 'quantum', text: 'Quantum Mechanical' },
                    { value: 'classical', text: 'Classical Methods' },
                    { value: 'hybrid', text: 'Hybrid Approach' }
                ])}
                ${this.createNumberInput(`precision_${this.featureId}`, 'Precision Level', '1', '10', '1')}
                ${this.createTextInput(`boundary_${this.featureId}`, 'Boundary Conditions', 'Specify conditions')}
                ${this.createCheckboxInput(`parallelProcessing_${this.featureId}`, 'Parallel Processing', true)}
            </div>
        `;
    }

    createFeature8Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createTextInput(`sampleId_${this.featureId}`, 'Sample ID', 'Enter sample identifier')}
                ${this.createSelectInput(`characterizationType_${this.featureId}`, 'Characterization Type', [
                    { value: 'structural', text: 'Structural Analysis' },
                    { value: 'compositional', text: 'Compositional Analysis' },
                    { value: 'property', text: 'Property Analysis' }
                ])}
                ${this.createNumberInput(`resolution_${this.featureId}`, 'Resolution (nm)', '0.1', '1000', '0.1')}
                ${this.createFileInput(`sampleData_${this.featureId}`, 'Sample Data File', '.dat,.csv')}
            </div>
        `;
    }

    createFeature11Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createTextInput(`materialSystem_${this.featureId}`, 'Material System', 'e.g., III-V, II-VI')}
                ${this.createSelectInput(`propertyPrediction_${this.featureId}`, 'Property to Predict', [
                    { value: 'bandgap', text: 'Band Gap' },
                    { value: 'mobility', text: 'Carrier Mobility' },
                    { value: 'conductivity', text: 'Electrical Conductivity' }
                ])}
                ${this.createNumberInput(`temperature_${this.featureId}`, 'Temperature (K)', '0', '1000', '1')}
                ${this.createCheckboxInput(`includeDefects_${this.featureId}`, 'Include Defects', false)}
            </div>
        `;
    }

    createFeature12Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createSelectInput(`bandCalculationType_${this.featureId}`, 'Band Calculation Type', [
                    { value: 'dft', text: 'DFT Calculation' },
                    { value: 'gw', text: 'GW Approximation' },
                    { value: 'hybrid', text: 'Hybrid Functional' }
                ])}
                ${this.createNumberInput(`kPoints_${this.featureId}`, 'K-Points Density', '1', '20', '1')}
                ${this.createTextInput(`latticeParams_${this.featureId}`, 'Lattice Parameters', 'a, b, c values')}
                ${this.createCheckboxInput(`spinOrbit_${this.featureId}`, 'Include Spin-Orbit Coupling', false)}
            </div>
        `;
    }

    createFeature13Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createSelectInput(`thermalProperty_${this.featureId}`, 'Thermal Property', [
                    { value: 'conductivity', text: 'Thermal Conductivity' },
                    { value: 'expansion', text: 'Thermal Expansion' },
                    { value: 'capacity', text: 'Heat Capacity' }
                ])}
                ${this.createNumberInput(`operatingPower_${this.featureId}`, 'Operating Power (W)', '0.1', '1000', '0.1')}
                ${this.createNumberInput(`ambientTemp_${this.featureId}`, 'Ambient Temperature (°C)', '-50', '200', '1')}
                ${this.createCheckboxInput(`includeConvection_${this.featureId}`, 'Include Convection', true)}
            </div>
        `;
    }

    createFeature14Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createSelectInput(`reliabilityTest_${this.featureId}`, 'Reliability Test', [
                    { value: 'thermal_cycling', text: 'Thermal Cycling' },
                    { value: 'humidity', text: 'Humidity Test' },
                    { value: 'voltage_stress', text: 'Voltage Stress' }
                ])}
                ${this.createNumberInput(`testDuration_${this.featureId}`, 'Test Duration (hours)', '1', '10000', '1')}
                ${this.createNumberInput(`failureCriteria_${this.featureId}`, 'Failure Criteria (%)', '1', '50', '1')}
                ${this.createCheckboxInput(`acceleratedTest_${this.featureId}`, 'Accelerated Testing', false)}
            </div>
        `;
    }

    createFeature15Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createSelectInput(`processStep_${this.featureId}`, 'Process Step', [
                    { value: 'deposition', text: 'Deposition' },
                    { value: 'etching', text: 'Etching' },
                    { value: 'annealing', text: 'Annealing' },
                    { value: 'doping', text: 'Doping' }
                ])}
                ${this.createNumberInput(`processTemp_${this.featureId}`, 'Process Temperature (°C)', '20', '1200', '10')}
                ${this.createTextInput(`gasFlow_${this.featureId}`, 'Gas Flow Rates', 'sccm values')}
                ${this.createCheckboxInput(`inSituMonitoring_${this.featureId}`, 'In-situ Monitoring', true)}
            </div>
        `;
    }

    createFeature16Inputs() {
        return `
            <p>Configure parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createSelectInput(`characterizationTech_${this.featureId}`, 'Characterization Technique', [
                    { value: 'xrd', text: 'X-ray Diffraction' },
                    { value: 'sem', text: 'SEM Imaging' },
                    { value: 'xps', text: 'XPS Analysis' },
                    { value: 'afm', text: 'AFM Measurement' }
                ])}
                ${this.createNumberInput(`scanRange_${this.featureId}`, 'Scan Range', '1', '1000', '1')}
                ${this.createFileInput(`referenceData_${this.featureId}`, 'Reference Data', '.ref,.std')}
                ${this.createCheckboxInput(`automaticAnalysis_${this.featureId}`, 'Automatic Analysis', true)}
            </div>
        `;
    }

    createDefaultInputs() {
        return `
            <p>Configure your input parameters for ${this.featureName}</p>
            <div class="input-controls">
                ${this.createTextInput(`parameter1_${this.featureId}`, 'Parameter 1', 'Enter value')}
                ${this.createSelectInput(`option1_${this.featureId}`, 'Option 1', [
                    { value: 'option_a', text: 'Option A' },
                    { value: 'option_b', text: 'Option B' },
                    { value: 'option_c', text: 'Option C' }
                ])}
                ${this.createNumberInput(`value1_${this.featureId}`, 'Numerical Value', '0', '100', '1')}
                ${this.createCheckboxInput(`enable1_${this.featureId}`, 'Enable Feature', true)}
            </div>
        `;
    }

    async processFeature() {
        // Simulate different processing results based on feature ID
        const processingResults = {
            4: {
                result1: 'Analysis completed - 95.2% accuracy',
                result2: 'Material properties calculated',
                result3: 'Report generated successfully'
            },
            5: {
                result1: 'Optimization converged in 45 iterations',
                result2: 'Performance improved by 23%',
                result3: 'Configuration saved'
            },
            6: {
                result1: 'Simulation completed successfully',
                result2: 'Model validation: 92% accuracy',
                result3: 'Predictions generated'
            },
            7: {
                result1: 'Computational analysis finished',
                result2: 'Discovery potential: High',
                result3: 'Results exported to database'
            },
            8: {
                result1: 'Comprehensive analysis complete',
                result2: 'Structure-property correlation: 0.87',
                result3: 'Visualization data ready'
            },
            11: {
                result1: 'Electronic properties predicted',
                result2: 'Band gap: 2.3 eV (direct)',
                result3: 'Mobility: 850 cm²/Vs'
            },
            12: {
                result1: 'Band structure calculated',
                result2: 'Transport properties computed',
                result3: 'DOS analysis completed'
            },
            13: {
                result1: 'Thermal management optimized',
                result2: 'Max temperature: 87°C',
                result3: 'Cooling solution recommended'
            },
            14: {
                result1: 'Reliability assessment completed',
                result2: 'MTTF: 15,000 hours',
                result3: 'Failure modes identified'
            },
            15: {
                result1: 'Process integration optimized',
                result2: 'Yield prediction: 89%',
                result3: 'Recipe parameters saved'
            },
            16: {
                result1: 'Characterization completed',
                result2: 'Material quality: Excellent',
                result3: 'Analysis report generated'
            }
        };

        return processingResults[this.featureId] || {
            result1: 'Processing completed successfully',
            result2: 'Analysis finished',
            result3: 'Results available'
        };
    }
}

// Create instances for each generic feature
window.Feature4 = class extends GenericFeature {
    constructor() { super(4, 'Feature 4', 'Advanced materials analysis and characterization tools for comprehensive evaluation'); }
};

window.Feature5 = class extends GenericFeature {
    constructor() { super(5, 'Feature 5', 'Materials optimization workflows for enhanced performance characteristics'); }
};

window.Feature6 = class extends GenericFeature {
    constructor() { super(6, 'Feature 6', 'Simulation and modeling tools for predicting material behavior under various conditions'); }
};

window.Feature7 = class extends GenericFeature {
    constructor() { super(7, 'Feature 7', 'Advanced computational methods for materials discovery and design'); }
};

window.Feature8 = class extends GenericFeature {
    constructor() { super(8, 'Feature 8', 'Comprehensive analysis tools for understanding material structure-property relationships'); }
};

window.Feature11 = class extends GenericFeature {
    constructor() { super(11, 'Feature 11', 'Electronic property prediction and optimization for semiconductor applications'); }
};

window.Feature12 = class extends GenericFeature {
    constructor() { super(12, 'Feature 12', 'Band structure calculations and electronic transport property analysis'); }
};

window.Feature13 = class extends GenericFeature {
    constructor() { super(13, 'Feature 13', 'Thermal management analysis for electronic device performance optimization'); }
};

window.Feature14 = class extends GenericFeature {
    constructor() { super(14, 'Feature 14', 'Reliability assessment and failure analysis for electronic materials'); }
};

window.Feature15 = class extends GenericFeature {
    constructor() { super(15, 'Feature 15', 'Process integration workflows for electronic device manufacturing'); }
};

window.Feature16 = class extends GenericFeature {
    constructor() { super(16, 'Feature 16', 'Advanced characterization techniques for electronic materials evaluation'); }
};
