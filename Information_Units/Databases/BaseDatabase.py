from pathlib import Path


# Base class for all databases
class BaseDatabase:
    def __init__(self, database_name='', logger=None):
        self.database_name = database_name
        self.logger=logger

    def info(self):
        return f'Information about database{self.database_name}'

    def retrieve(self, inputs: dict) -> str:
        """
        Retrieve data from database.
        Args:
            inputs (dict): Parsed input values from frontend
        Returns:
            Retrieved materials (to be implemented by subclasses)
        """
        raise NotImplementedError("Subclasses must implement retrieve()")


