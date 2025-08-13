def process(input_data):
    """
    Process material search with user inputs
    Args:
        input_data (dict): User input values from the form
    Returns:
        dict: Results matching the feature's expected output format
    """
    # Extract inputs with defaults
    material_name = input_data.get('materialName', '')
    property_type = input_data.get('propertyType', 'mechanical')
    min_value = input_data.get('minValue', '0')
    max_value = input_data.get('maxValue', '100')
    crystal_system = input_data.get('crystalSystem', 'cubic')
    
    # Processing logic based on inputs
    # ... (left empty as requested) ...
    
    # Return results matching MaterialSearch.js output format with 'python' string
    return {
        'materialsCount': '42 materials found - python',
        'topMatch': 'Silicon Carbide (SiC) - python',
        'propertyRange': '2.5 - 45.2 GPa - python',
        'downloadLink': 'search_results.csv (Ready) - python'
    }
