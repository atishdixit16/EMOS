from flask import Flask, request, jsonify
from flask_cors import CORS
import importlib.util
import os
import sys

app = Flask(__name__)
CORS(app)

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@app.route('/api/process/3', methods=['POST'])
def process_database_extractor():
    try:
        # Load the Database Extractor processor module
        processor_path = os.path.join('..', 'Features', 'Materials_Exploration', 'Database_Extractor', 'processor.py')
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
    print("Starting Flask server for Database Extractor...")
    print("Database Extractor endpoint: http://localhost:5001/api/process/3")
    app.run(debug=True, port=5001)
