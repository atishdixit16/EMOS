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
    
    # Processing logic based on inputs
    if logger:
        logger.log('Material generation process - python', 'info')
    
    # Return results matching MaterialGeneration.js output format with 'python' string
    return {
        'generatedCount': '15 compositions generated - python',
        'bestCandidate': 'Ti3Al2C (MAX Phase) - python',
        'predictedPerformance': '8.5 GPa (92% of target) - python',
        'synthesisDifficulty': 'Medium - python',
        'exportData': 'compositions.json (Ready) - python'
    }
