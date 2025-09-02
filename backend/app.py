from flask import Flask, request, jsonify
from flask_cors import CORS
import importlib.util
import os
import sys
import pathlib

# Get absolute paths regardless of where the script is run from
BACKEND_DIR = pathlib.Path(__file__).parent.resolve()  # /home/soe/EMOS/backend
PROJECT_ROOT = BACKEND_DIR.parent.resolve()  # /home/soe/EMOS

# Add the project root to Python path
sys.path.append(str(PROJECT_ROOT))

#generator creators & destroyers
from Information_Units.Generators.GeneratorFactory import generator_factory, generator_registry

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Ensure CORS headers even on errors
@app.after_request
def add_cors_headers(response):
    origin = request.headers.get('Origin')
    response.headers['Access-Control-Allow-Origin'] = origin or '*'
    response.headers['Vary'] = 'Origin'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

# Simple logger class
class SimpleLogger:
    def __init__(self):
        self.logs = []
    
    def log(self, message, level='info'):
        self.logs.append({
            'message': message,
            'level': level
        })
    
    def get_logs(self):
        return self.logs
    
# Create universal logger
logger = SimpleLogger()

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


@app.route('/api/health', methods=['GET', 'OPTIONS'])
def health():
    return jsonify({'status': 'ok'}), 200


@app.route('/api/process/toggle_generator', methods=["POST", "OPTIONS"])
def toggle_generator():
    if request.method == 'OPTIONS':
        return ('', 204)
    try:
        data = request.get_json() or {}
        class_name = data.get("class_name")
        active = data.get("active")

        if not class_name:
            return jsonify({"message": "Missing class_name"}), 400
        if active is None:
            return jsonify({"message": "Missing active"}), 400
        if class_name not in generator_factory:
            return jsonify({"message": "Unknown class"}), 400

        if active:
            # Instantiate and store
            cls = generator_factory[class_name]
            instance = cls(class_name, logger)  # will raise if factory mapped to an instance
            generator_registry[class_name] = instance
            return jsonify({"message": f"{class_name} instantiated"})
        else:
            generator_registry.pop(class_name, None)
            return jsonify({"message": f"{class_name} removed"})
    except TypeError as e:
        # Most common: factory mapped to an instance, not a class
        return jsonify({"message": f"Instantiation failed for {class_name}: {e}"}), 500
    except Exception as e:
        return jsonify({"message": f"Toggle failed: {e}"}), 500


@app.route('/api/process/<int:feature_id>', methods=['POST'])
def process_feature(feature_id):
    try:
        # Get the feature path
        if feature_id not in FEATURE_PATHS:
            return jsonify({'error': f'Feature {feature_id} not found'}), 404
        
        # Construct absolute path to processor.py
        processor_path = PROJECT_ROOT / FEATURE_PATHS[feature_id] / 'processor.py'
        
        # Debug info
        print(f"Project root: {PROJECT_ROOT}")
        print(f"Looking for processor at: {processor_path}")
        print(f"File exists: {processor_path.exists()}")
        
        if not processor_path.exists():
            return jsonify({'error': f'Processor file not found: {processor_path}'}), 404
        
        # Load the processor module
        spec = importlib.util.spec_from_file_location("processor", str(processor_path))
        processor_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(processor_module)
        
        # Get input data and process
        input_data = request.json or {}
        
        # Try to pass logger to processor
        try:
            results = processor_module.process(input_data, logger)
        except TypeError:
            # Fallback if processor doesn't accept logger
            results = processor_module.process(input_data)
        
        # Return results with logs
        return jsonify({
            'results': results,
            'logs': logger.get_logs()
        })
        
    except Exception as e:
        print(f"Error in process_feature: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server for all EMOS features...")
    print(f"Project root: {PROJECT_ROOT}")
    print("Available endpoints:")
    for feature_id, path in FEATURE_PATHS.items():
        full_path = PROJECT_ROOT / path / 'processor.py'
        status = "✅" if full_path.exists() else "❌"
        print(f"  {status} Feature {feature_id}: http://localhost:5001/api/process/{feature_id}")
    app.run(debug=True, port=5001)
