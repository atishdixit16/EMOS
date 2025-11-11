from Information_Units.Predictors.BasePredictor import BasePredictor

class MattersimPredictor(BasePredictor):
    def __init__(self, predictor_name, logger=None):
        super().__init__(predictor_name, logger)

    def info(self):
        msg="MatterSim, the MLIP for inorganic crystals, created by Microsoft"
        return msg

    def predict(self, input_data):
        # Implement prediction logic here
        # For now, just simulate prediction results
        if self.logger:
            self.logger.log("Predicted by MatterSim - python", 'info')
        
        return None
