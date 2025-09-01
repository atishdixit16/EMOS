def process(input_data, logger=None):
    """
    Process interface calculation with user inputs
    Args:
        input_data (dict): User input values from the form
        logger: Optional logger for capturing logs
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
    
    # Extract and log active databases
    active_databases = input_data.get('active_databases', [])
    # Extract and log active generators
    active_generators = input_data.get('active_generators', [])
    # Extract and log active predictors
    active_predictors = input_data.get('active_predictors', [])
    
    if logger:
        logger.log('Initializing interface calculation...', 'info')
        
        # Log active databases
        if not active_databases:
            logger.log('No active databases found.', 'warning')
        else:
            database_names = ', '.join(db["name"] for db in active_databases)
            logger.log(f'Active databases ({len(active_databases)}): {database_names}', 'info')
    
        # Log active generators
        if not active_generators:
            logger.log('No active generators found.', 'warning')
        else:
            generator_names = ', '.join(gen["name"] for gen in active_generators)
            logger.log(f'Active generators ({len(active_generators)}): {generator_names}', 'info')
        
        # Log active predictors
        if not active_predictors:
            logger.log('No active predictors found.', 'warning')
        else:
            predictor_names = ', '.join(pred["name"] for pred in active_predictors)
            logger.log(f'Active predictors ({len(active_predictors)}): {predictor_names}', 'info')
        
        logger.log('Interface calculation process - python', 'info')
    
    # Processing logic based on inputs
    
    # Return results matching InterfaceCalculation.js output format with 'python' string
    return {
        'interfaceEnergy': '1.247 J/m² - python',
        'bandOffset': '1.85 eV - python',
        'latticeMismatch': '2.3% - python',
        'interfaceStates': '3.24e12 states/cm² - python',
        'chargeTransfer': '0.285 e⁻ - python'
    }
