from Information_Units.Databases.BaseDatabase import BaseDatabase

# Example generator subclasses
class IcsdDatabase(BaseDatabase):
    def __init__(self, database_name, logger=None):
        super().__init__(database_name, logger)
    
    def info(self):
        msg="ICSD: Inorganic Crystal Structure Database, the world's largest database for inorganic crystal structures"
        return msg

    def retrieve(self, inputs: dict) -> str:
        # Implement retrieval logic here
        # For now, just simulate a path
        if self.logger:
            self.logger.log("Retrieved from ICSD")
        return None
