from Features.BaseFeature import BaseFeature
from Information_Units.Generators.GeneratorFactory import generator_factory
from Information_Units.Databases.DatabaseFactory import database_factory
from Information_Units.Predictors.PredictorFactory import predictor_factory


class InterfaceCalculationFeature(BaseFeature):
    def __init__(self, logger=None):
        super().__init__("Interface Calculation", logger)
    
    def info(self):
        return "Interface Calculation: Calculate interface properties and band alignments"
    
    def extract_inputs(self, input_data):
        return {
            'interface_type': input_data.get('interfaceType', 'metal-semiconductor'),
            'material_a': input_data.get('materialA', 'Al'),
            'material_b': input_data.get('materialB', 'Si'),
            'calculation_method': input_data.get('calculationMethod', 'DFT'),
            'active_databases': input_data.get('active_databases', []),
            'active_generators': input_data.get('active_generators', []),
            'active_predictors': input_data.get('active_predictors', [])
        }
    
    def process_feature(self, inputs):
        if self.logger:
            self.logger.log('Initializing interface calculation...', 'info')
        
        self._process_information_units(inputs)
        
        if self.logger:
            self.logger.log('Interface calculation process - python', 'info')
        
        return {
            'interface_results': f"{inputs['interface_type']} interface between {inputs['material_a']}/{inputs['material_b']}",
            'calculation_method': inputs['calculation_method'],
            'band_alignment': "Type-II band alignment calculated"
        }
    
    def format_outputs(self, processed_results):
        """Format the final output results"""
        return {
            'interfaceEnergy': '1.247 J/m² - python',
            'bandOffset': '1.85 eV - python',
            'latticeMismatch': '2.3% - python',
            'interfaceStates': '3.24e12 states/cm² - python',
            'chargeTransfer': '0.285 e⁻ - python'
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
                    retrieve_inputs = {'interface_type': inputs['interface_type']}
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
                    generate_inputs = {'materials': f"{inputs['material_a']}/{inputs['material_b']}"}
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
                    predict_inputs = {'interface': inputs['interface_type']}
                    try:
                        pred_instance.predict(predict_inputs)
                    except Exception as e:
                        if self.logger:
                            self.logger.log(f'Predictor {pred_key} predict() error: {str(e)}', 'warning')