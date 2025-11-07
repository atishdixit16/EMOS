from Features.BaseFeature import BaseFeature
from Information_Units.Generators.GeneratorFactory import generator_factory
from Information_Units.Databases.DatabaseFactory import database_factory
from Information_Units.Predictors.PredictorFactory import predictor_factory


class MaterialCharacterizationFeature(BaseFeature):
    def __init__(self, feature_id, logger=None):
        super().__init__(feature_id, 'Material Characterization', logger)
    
    def info(self):
        return f"Feature {self.feature_id}: {self.feature_name} - Advanced material property characterization and analysis"
    
    def extract_inputs(self, input_data):
        """Extract and validate input parameters"""
        return {
            'material_id': input_data.get('materialId', 'MP-123'),
            'characterization_method': input_data.get('characterizationMethod', 'XRD'),
            'temperature': input_data.get('temperature', '298'),
            'pressure': input_data.get('pressure', '1'),
            'active_databases': input_data.get('active_databases', []),
            'active_generators': input_data.get('active_generators', []),
            'active_predictors': input_data.get('active_predictors', [])
        }
    
    def process_feature(self, inputs):
        """Perform the core material characterization logic"""
        if self.logger:
            self.logger.log('Initializing material characterization...', 'info')
        
        # Process Information Units
        self._process_information_units(inputs)
        
        if self.logger:
            self.logger.log('Material characterization process - python', 'info')
        
        return {
            'characterization_results': f"Characterized {inputs['material_id']} using {inputs['characterization_method']}",
            'conditions': f"T={inputs['temperature']}K, P={inputs['pressure']}atm",
            'method': inputs['characterization_method']
        }
    
    def format_outputs(self, processed_results):
        """Format the final output results"""
        return {
            'characterizationStatus': 'Material characterization completed - python',
            'physicalProperties': 'Density: 4.23 g/cm³, Hardness: 7.2 GPa - python',
            'opticalProperties': 'Band gap: 3.2 eV, Refractive index: 2.47 - python',
            'reportGenerated': 'Comprehensive analysis report ready - python'
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
                    retrieve_inputs = {'material_id': inputs['material_id']}
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
                    generate_inputs = {'material_type': inputs['material_id']}
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
                    predict_inputs = {'material_id': inputs['material_id']}
                    try:
                        pred_instance.predict(predict_inputs)
                    except Exception as e:
                        if self.logger:
                            self.logger.log(f'Predictor {pred_key} predict() error: {str(e)}', 'warning')