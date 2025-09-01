def process(input_data, logger=None):
    """
    Process material search with user inputs
    Args:
        input_data (dict): User input values from the form
        logger: Optional logger for capturing logs
    Returns:
        dict: Results matching the feature's expected output format
    """
    # Extract inputs with defaults
    material_name = input_data.get('materialName', '')
    property_type = input_data.get('propertyType', 'mechanical')
    min_value = input_data.get('minValue', '0')
    max_value = input_data.get('maxValue', '100')
    crystal_system = input_data.get('crystalSystem', 'cubic')
    
    # Extract and log active databases
    active_databases = input_data.get('active_databases', [])
    # Extract and log active generators
    active_generators = input_data.get('active_generators', [])
    # Extract and log active predictors
    active_predictors = input_data.get('active_predictors', [])
    
    if logger:
        logger.log('Initializing material search...', 'info')
        
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
        
        logger.log('Material search process - python', 'info')
    
    # Processing logic based on inputs
    
    # Return results matching MaterialSearch.js output format with 'python' string
    return {
        'materialsCount': '42 materials found - python',
        'topMatch': 'Silicon Carbide (SiC) - python',
        'propertyRange': '2.5 - 45.2 GPa - python',
        'downloadLink': 'search_results.csv (Ready) - python'
    }
