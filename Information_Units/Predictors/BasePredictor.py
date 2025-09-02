from pathlib import Path


# Base class for all generators
class BasePredictor:
    def __init__(self, predictor_name='', logger=None):
        self.predictor_name = predictor_name
        self.logger=logger

    def info(self):
        return f'Information about predictor {self.predictor_name}'

    def predict(self, inputs: dict) -> str:
        """
        Predict properties.
        Args:
            inputs (dict): Parsed input values from frontend
        Returns:
            Predicted properties (to be implemented by subclasses)
        """
        raise NotImplementedError("Subclasses must implement predict()")


