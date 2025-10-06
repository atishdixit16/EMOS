from Information_Units.Generators.GeneratorFactory import generator_factory
from Information_Units.Databases.DatabaseFactory import database_factory
from Information_Units.Predictors.PredictorFactory import predictor_factory


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
    
    # Template for processing logic based on inputs and information units

    # Process active databases
    if not active_databases:
        if logger:
            logger.log('No active databases found.', 'warning')
    else:
        if logger:
            database_names = ', '.join(db["name"] for db in active_databases)
            logger.log(f'Active databases ({len(active_databases)}): {database_names}', 'info')
        
        for dtbs in active_databases:
            db_key = dtbs['value']
            if db_key in database_factory:
                # Create instance and call retrieve method
                db_instance = database_factory[db_key](db_key, logger)
                if logger:
                    logger.log(db_instance.info(), 'info')
                # Demonstrate the retrieve functionality
                retrieve_inputs = {'query': material_name, 'property': property_type, 'crystal_system': crystal_system}
                try:
                    result = db_instance.retrieve(retrieve_inputs)
                except Exception as e:
                    if logger:
                        logger.log(f'Database {db_key} retrieve() error: {str(e)}', 'warning')
            else:
                if logger:
                    logger.log(f'Database {db_key} not found in factory', 'warning')

    # Process active generators
    if not active_generators:
        if logger:
            logger.log('No active generators found.', 'warning')
    else:
        if logger:
            generator_names = ', '.join(gen["name"] for gen in active_generators)
            logger.log(f'Active generators ({len(active_generators)}): {generator_names}', 'info')
        
        for gnrtr in active_generators:
            gen_key = gnrtr['value']
            if gen_key in generator_factory:
                # Create instance and call generate method
                gen_instance = generator_factory[gen_key](gen_key, logger)
                if logger:
                    logger.log(gen_instance.info(), 'info')
                # Demonstrate the generate functionality
                generate_inputs = {
                    'property_type': property_type, 
                    'crystal_system': crystal_system,
                    'value_range': f'{min_value}-{max_value}'
                }
                try:
                    result = gen_instance.generate(generate_inputs)
                except Exception as e:
                    if logger:
                        logger.log(f'Generator {gen_key} generate() error: {str(e)}', 'warning')
            else:
                if logger:
                    logger.log(f'Generator {gen_key} not found in factory', 'warning')
    
    # Process active predictors
    if not active_predictors:
        if logger:
            logger.log('No active predictors found.', 'warning')
    else:
        if logger:
            predictor_names = ', '.join(pred["name"] for pred in active_predictors)
            logger.log(f'Active predictors ({len(active_predictors)}): {predictor_names}', 'info')
        
        for prdctr in active_predictors:
            pred_key = prdctr['value']
            if pred_key in predictor_factory:
                # Create instance and call predict method
                pred_instance = predictor_factory[pred_key](pred_key, logger)
                if logger:
                    logger.log(pred_instance.info(), 'info')
                # Demonstrate the predict functionality
                predict_inputs = {
                    'material': material_name,
                    'property_type': property_type,
                    'min_value': min_value,
                    'max_value': max_value
                }
                try:
                    result = pred_instance.predict(predict_inputs)
                except Exception as e:
                    if logger:
                        logger.log(f'Predictor {pred_key} predict() error: {str(e)}', 'warning')
            else:
                if logger:
                    logger.log(f'Predictor {pred_key} not found in factory', 'warning')
    
    if logger:
        logger.log('Material search process - python', 'info')
    
    # Return results matching MaterialSearch.js output format with 'python' string
    return {
        'materialsCount': '42 materials found - python',
        'topMatch': 'Silicon Carbide (SiC) - python',
        'propertyRange': '2.5 - 45.2 GPa - python',
        'downloadLink': 'search_results.csv (Ready) - python'
    }
