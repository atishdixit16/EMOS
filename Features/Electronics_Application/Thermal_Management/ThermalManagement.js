// Thermal Management
class ThermalManagementFeature extends BaseFeature {
    constructor() {
        super(13, 'Thermal Management', 'Thermal management analysis for electronic device performance optimization');
    }

    createInputsHTML() {
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

    async processFeature() {
        await this.simulateProcessing();
        
        return {
            result1: 'Thermal management optimized',
            result2: 'Max temperature: 87°C',
            result3: 'Cooling solution recommended'
        };
    }
}

window.ThermalManagementFeature = ThermalManagementFeature;
