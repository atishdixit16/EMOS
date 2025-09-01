def process(input_data, logger=None):
    """
    Process database extraction with user inputs
    Args:
        input_data (dict): User input values from the form
        logger: Optional logger for capturing logs
    Returns:
        dict: Results matching the feature's expected output format
    """
    # Extract inputs with defaults
    database_source = input_data.get('databaseSource', 'all')
    extraction_type = input_data.get('extractionType', 'properties')
    filter_criteria = input_data.get('filterCriteria', '')
    max_entries = input_data.get('maxEntries', '1000')
    include_metadata = input_data.get('includeMetadata', True)
    
    # Extract and log active databases
    active_databases = input_data.get('active_databases', [])
    # Extract and log active generators
    active_generators = input_data.get('active_generators', [])
    # Extract and log active predictors
    active_predictors = input_data.get('active_predictors', [])
    
    if logger:
        logger.log('Initializing database extraction...', 'info')
        
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
        
        logger.log('Database extraction process - python', 'info')
    
    # Processing logic based on inputs
    
    # Return results matching DatabaseExtractor.js output format with 'python' string
    return {
        'recordsExtracted': '2,847 records - python',
        'dataSize': '425.3 MB - python',
        'fileFormat': 'JSON with metadata - python',
        'processingTime': '28.5 seconds - python',
        'downloadPackage': 'extracted_data.zip (Ready) - python'
    }
