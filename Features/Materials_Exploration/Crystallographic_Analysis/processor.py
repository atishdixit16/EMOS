from Information_Units.Generators.GeneratorFactory import generator_factory
from Information_Units.Databases.DatabaseFactory import database_factory
from Information_Units.Predictors.PredictorFactory import predictor_factory


def process(input_data, logger=None):
    """
    Process crystallographic analysis with user inputs
    Args:
        input_data (dict): User input values from the form
        logger: Optional logger for capturing logs
    Returns:
        dict: Results matching the feature's expected output format
    """

    """
    Process crystallographic analysis with user inputs
    Args:
        input_data (dict): User input values from the form
        logger: Optional logger for capturing logs
    Returns:
        dict: Results matching the feature's expected output format
    """
    # Extract inputs with defaults
    optimization_target = input_data.get('optimizationTarget', 'performance')
    iterations = input_data.get('iterations', '100')
    config_file = input_data.get('configFile', '')
    verbose_output = input_data.get('verboseOutput', False)
    
        
    # Extract and log active databases
    active_databases = input_data.get('active_databases', [])
    # Extract and log active generators
    active_generators = input_data.get('active_generators', [])
    # Extract and log active predictors
    active_predictors = input_data.get('active_predictors', [])
    
    if logger:
        logger.log('Initializing crystallographic analysis...', 'info')

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
                retrieve_inputs = {'query': 'general'}
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
                generate_inputs = {'target': 'default'}
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
                predict_inputs = {'input': 'default'}
                try:
                    result = pred_instance.predict(predict_inputs)
                except Exception as e:
                    if logger:
                        logger.log(f'Predictor {pred_key} predict() error: {str(e)}', 'warning')
            else:
                if logger:
                    logger.log(f'Predictor {pred_key} not found in factory', 'warning')
    
    if logger:
        logger.log('crystallographic analysis process - python', 'info')
    
    # Return results matching CrystallographicAnalysis.js output format with 'python' string
    return {
        'simulationStatus': 'Simulation completed successfully - python',
        'modelValidation': 'Model validation: 91.3% accuracy - python',
        'predictions': 'Structural predictions generated - python'
    }
