from Information_Units.Generators.GeneratorFactory import generator_registry
from Information_Units.Databases.DatabaseFactory import database_registry
from Information_Units.Predictors.PredictorFactory import predictor_registry


def process(input_data, logger=None):
    """
    Process material generation with user inputs
    Args:
        input_data (dict): User input values from the form
        logger: Optional logger for capturing logs
    Returns:
        dict: Results matching the feature's expected output format
    """
    # Extract inputs with defaults
    target_property = input_data.get('targetProperty', 'high_strength')
    base_elements = input_data.get('baseElements', 'metals')
    num_compositions = input_data.get('numCompositions', '10')
    target_value = input_data.get('targetValue', '100')
    include_rare_elements = input_data.get('includeRareElements', False)
    optimize_for_cost = input_data.get('optimizeForCost', True)
    
    # Extract and log active databases
    active_databases = input_data.get('active_databases', [])
    # Extract and log active generators
    active_generators = input_data.get('active_generators', [])
    # Extract and log active predictors
    active_predictors = input_data.get('active_predictors', [])
    
    if logger:
        logger.log('Initializing material generation...', 'info')
        
        # Log active databases
        if not active_databases:
            logger.log('No active databases found.', 'warning')
        else:
            database_names = ', '.join(db["name"] for db in active_databases)
            logger.log(f'Active databases ({len(active_databases)}): {database_names}', 'info')
            for dtbs in active_databases:
                logger.log(database_registry[dtbs['value']].info(), 'info')
    
        # Log active generators
        if not active_generators:
            logger.log('No active generators found.', 'warning')
        else:
            generator_names = ', '.join(gen["name"] for gen in active_generators)
            logger.log(f'Active generators ({len(active_generators)}): {generator_names}', 'info')
            for gnrtr in active_generators:
                logger.log(generator_registry[gnrtr['value']].info(), 'info')
        
        # Log active predictors
        if not active_predictors:
            logger.log('No active predictors found.', 'warning')
        else:
            predictor_names = ', '.join(pred["name"] for pred in active_predictors)
            logger.log(f'Active predictors ({len(active_predictors)}): {predictor_names}', 'info')
            for prdctr in active_predictors:
                logger.log(predictor_registry[prdctr['value']].info(), 'info')
        
        logger.log('Material generation process - python', 'info')
    
    # Processing logic based on inputs
    output_files=[]
    for gnrtr in active_generators:
        output_files.append(generator_registry[gnrtr['value']].generate(input_data))

    
    # Return results matching MaterialGeneration.js output format with 'python' string
    return {
        'generatedCount': '15 compositions generated - python',
        'bestCandidate': 'Ti3Al2C (MAX Phase) - python',
        'predictedPerformance': '8.5 GPa (92% of target) - python',
        'synthesisDifficulty': 'Medium - python',
        'exportData': f'{str(output_files)} (Ready) - python'
    }
