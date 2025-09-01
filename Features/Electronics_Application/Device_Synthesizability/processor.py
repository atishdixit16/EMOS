def process(input_data, logger=None):
    """
    Process device synthesizability with user inputs
    Args:
        input_data (dict): User input values from the form
        logger: Optional logger for capturing logs
    Returns:
        dict: Results matching the feature's expected output format
    """
    # Extract inputs with defaults
    device_type = input_data.get('deviceType', 'transistor')
    material_composition = input_data.get('materialComposition', '')
    substrate_type = input_data.get('substrateType', 'silicon')
    operating_temp = input_data.get('operatingTemp', '25')
    fabrication_method = input_data.get('fabricationMethod', 'mocvd')
    
    # Extract and log active databases
    active_databases = input_data.get('active_databases', [])
    # Extract and log active generators
    active_generators = input_data.get('active_generators', [])
    # Extract and log active predictors
    active_predictors = input_data.get('active_predictors', [])
    
    if logger:
        logger.log('Initializing device synthesizability...', 'info')
        
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
        
        logger.log('Device synthesizability process - python', 'info')
    
    # Processing logic based on inputs
    
    # Return results matching DeviceSynthesizability.js output format with 'python' string
    return {
        'feasibility': '78% (High) - python',
        'recommendedProcess': 'MOCVD with 3-step annealing - python',
        'estimatedCost': '$245/wafer - python',
        'processTemp': '650°C - python',
        'yieldPrediction': '85% - python'
    }
