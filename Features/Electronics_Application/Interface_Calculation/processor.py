def process(input_data):
    """
    Process interface calculation with user inputs
    Args:
        input_data (dict): User input values from the form
    Returns:
        dict: Results matching the feature's expected output format
    """
    # Extract inputs with defaults
    material1 = input_data.get('material1', '')
    material2 = input_data.get('material2', '')
    interface_type = input_data.get('interfaceType', 'coherent')
    calculation_method = input_data.get('calculationMethod', 'dft')
    supercell_size = input_data.get('supercellSize', '100')
    include_strain = input_data.get('includeStrain', True)
    calculate_band_offset = input_data.get('calculateBandOffset', True)
    
    # Processing logic based on inputs
    # ... (left empty as requested) ...
    
    # Return results matching InterfaceCalculation.js output format with 'python' string
    return {
        'interfaceEnergy': '1.247 J/m² - python',
        'bandOffset': '1.85 eV - python',
        'latticeMismatch': '2.3% - python',
        'interfaceStates': '3.24e12 states/cm² - python',
        'chargeTransfer': '0.285 e⁻ - python'
    }
