from abc import ABC, abstractmethod


class BaseFeature(ABC):
    """Simple base class for all Features - minimal implementation"""
    
    def __init__(self, feature_name, logger=None):
        self.feature_name = feature_name
        self.logger = logger
    
    @abstractmethod
    def info(self):
        """Return feature description"""
        pass
    
    @abstractmethod
    def extract_inputs(self, input_data):
        """Extract and validate inputs from input_data"""
        pass
    
    @abstractmethod
    def process_feature(self, inputs):
        """Core feature processing logic"""
        pass
    
    @abstractmethod
    def format_outputs(self, results):
        """Format results to expected output format"""
        pass
    
    def process(self, input_data):
        """Main process method - template pattern"""
        # Step 1: Extract inputs
        inputs = self.extract_inputs(input_data)
        
        # Step 2: Process feature
        results = self.process_feature(inputs)
        
        # Step 3: Format outputs
        outputs = self.format_outputs(results)
        
        return outputs