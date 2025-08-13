from flask import Flask, request, jsonify
from flask_cors import CORS
import importlib.util
import os
import sys

app = Flask(__name__)
CORS(app)

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Feature ID to folder mapping
FEATURE_PATHS = {
    1: 'Features/Materials_Exploration/Material_Search',
    2: 'Features/Materials_Exploration/Material_Generation',
    3: 'Features/Materials_Exploration/Database_Extractor',
    4: 'Features/Materials_Exploration/Material_Characterization',
    5: 'Features/Materials_Exploration/DFT_Calculation',
    6: 'Features/Materials_Exploration/Crystallographic_Analysis',
    7: 'Features/Materials_Exploration/Quantum_Mechanics',
    8: 'Features/Materials_Exploration/Tensor_Analysis',
    9: 'Features/Electronics_Application/Device_Synthesizability',
    10: 'Features/Electronics_Application/Interface_Calculation',
    11: 'Features/Electronics_Application/Property_Prediction',
    12: 'Features/Electronics_Application/Band_Structure',
    13: 'Features/Electronics_Application/Thermal_Management',
    14: 'Features/Electronics_Application/Reliability_Assessment',
    15: 'Features/Electronics_Application/Process_Integration',
    16: 'Features/Electronics_Application/Advanced_Characterization'
}

@app.route('/api/process/<int:feature_id>', methods=['POST'])
def process_feature(feature_id):
    try:
        # Get the feature path
        if feature_id not in FEATURE_PATHS:
            return jsonify({'error': f'Feature {feature_id} not found'}), 404
        
        # Load the processor module
        processor_path = os.path.join('..', FEATURE_PATHS[feature_id], 'processor.py')
        processor_path = os.path.abspath(processor_path)
        
        spec = importlib.util.spec_from_file_location("processor", processor_path)
        processor_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(processor_module)
        
        # Get input data and process
        input_data = request.json or {}
        results = processor_module.process(input_data)
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server for all EMOS features...")
    print("Available endpoints:")
    for feature_id, path in FEATURE_PATHS.items():
        print(f"  Feature {feature_id}: http://localhost:5001/api/process/{feature_id}")
    app.run(debug=True, port=5001)
