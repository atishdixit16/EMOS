from pathlib import Path


# Base class for all generators
class BaseGenerator:
    def __init__(self, generator_name):
        self.generator_name = generator_name

    def generate(self, inputs: dict) -> str:
        """
        Generate output based on parsed inputs.
        Args:
            inputs (dict): Parsed input values from frontend
        Returns:
            str: Path to generated output (to be implemented by subclasses)
        """
        raise NotImplementedError("Subclasses must implement generate()")


