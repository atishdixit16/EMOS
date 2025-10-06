from Features.BaseFeature import BaseFeature
from Information_Units.Generators.GeneratorFactory import generator_factory
from Information_Units.Databases.DatabaseFactory import database_factory
from Information_Units.Predictors.PredictorFactory import predictor_factory


class MaterialGenerationFeature(BaseFeature):
    def __init__(self, logger=None):
        super().__init__("Material Generation", logger)
    
    def info(self):
        return "Material Generation: Generate new materials with desired properties using AI and ML models"
    
    def extract_inputs(self, input_data):
        return {
            'target_property': input_data.get('targetProperty', 'high_strength'),
            'base_elements': input_data.get('baseElements', 'metals'),
            'temperature': input_data.get('temperature', '300'),
            'pressure': input_data.get('pressure', '1'),
            'active_databases': input_data.get('active_databases', []),
            'active_generators': input_data.get('active_generators', []),
            'active_predictors': input_data.get('active_predictors', [])
        }
    
    def process_feature(self, inputs):
        if self.logger:
            self.logger.log('Initializing material generation...', 'info')
        
        self._process_information_units(inputs)
        
        if self.logger:
            self.logger.log('Material generation process - python', 'info')
        
        return {
            'generated_materials': f"Generated materials with {inputs['target_property']}",
            'base_elements': inputs['base_elements'],
            'conditions': f"T={inputs['temperature']}K, P={inputs['pressure']}atm"
        }
    
    def format_outputs(self, processed_results):
        """Format the final output results"""
        return {
            'generatedCount': '15 compositions generated - python',
            'bestCandidate': 'Ti3Al2C (MAX Phase) - python',
            'predictedPerformance': '8.5 GPa (92% of target) - python',
            'synthesisDifficulty': 'Medium - python',
            'exportData': 'Generated materials ready for export - python'
        }
    
    def _process_information_units(self, inputs):
        # Process databases
        active_databases = inputs.get('active_databases', [])
        if not active_databases:
            if self.logger:
                self.logger.log('No active databases found.', 'warning')
        else:
            if self.logger:
                database_names = ', '.join(db["name"] for db in active_databases)
                self.logger.log(f'Active databases ({len(active_databases)}): {database_names}', 'info')
            
            for dtbs in active_databases:
                db_key = dtbs['value']
                if db_key in database_factory:
                    db_instance = database_factory[db_key](db_key, self.logger)
                    if self.logger:
                        self.logger.log(db_instance.info(), 'info')
                    retrieve_inputs = {'target_property': inputs['target_property']}
                    try:
                        db_instance.retrieve(retrieve_inputs)
                    except Exception as e:
                        if self.logger:
                            self.logger.log(f'Database {db_key} retrieve() error: {str(e)}', 'warning')
        
        # Process generators
        active_generators = inputs.get('active_generators', [])
        if not active_generators:
            if self.logger:
                self.logger.log('No active generators found.', 'warning')
        else:
            if self.logger:
                generator_names = ', '.join(gen["name"] for gen in active_generators)
                self.logger.log(f'Active generators ({len(active_generators)}): {generator_names}', 'info')
            
            for gnrtr in active_generators:
                gen_key = gnrtr['value']
                if gen_key in generator_factory:
                    gen_instance = generator_factory[gen_key](gen_key, self.logger)
                    if self.logger:
                        self.logger.log(gen_instance.info(), 'info')
                    generate_inputs = {
                        'target_property': inputs['target_property'],
                        'base_elements': inputs['base_elements']
                    }
                    try:
                        gen_instance.generate(generate_inputs)
                    except Exception as e:
                        if self.logger:
                            self.logger.log(f'Generator {gen_key} generate() error: {str(e)}', 'warning')
        
        # Process predictors
        active_predictors = inputs.get('active_predictors', [])
        if not active_predictors:
            if self.logger:
                self.logger.log('No active predictors found.', 'warning')
        else:
            if self.logger:
                predictor_names = ', '.join(pred["name"] for pred in active_predictors)
                self.logger.log(f'Active predictors ({len(active_predictors)}): {predictor_names}', 'info')
            
            for prdctr in active_predictors:
                pred_key = prdctr['value']
                if pred_key in predictor_factory:
                    pred_instance = predictor_factory[pred_key](pred_key, self.logger)
                    if self.logger:
                        self.logger.log(pred_instance.info(), 'info')
                    predict_inputs = {
                        'target_property': inputs['target_property'],
                        'temperature': inputs['temperature']
                    }
                    try:
                        pred_instance.predict(predict_inputs)
                    except Exception as e:
                        if self.logger:
                            self.logger.log(f'Predictor {pred_key} predict() error: {str(e)}', 'warning')