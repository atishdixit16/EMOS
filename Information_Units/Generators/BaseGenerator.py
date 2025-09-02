from pathlib import Path


# Base class for all generators
class BaseGenerator:
    def __init__(self, generator_name='', logger=None):
        self.generator_name = generator_name
        self.logger=logger

    def info(self):
        return f'Information about generator {self.generator_name}'

    def generate(self, inputs: dict) -> str:
        """
        Generate output based on parsed inputs.
        Args:
            inputs (dict): Parsed input values from frontend
        Returns:
            str: Path to generated output (to be implemented by subclasses)
        """
        raise NotImplementedError("Subclasses must implement generate()")


