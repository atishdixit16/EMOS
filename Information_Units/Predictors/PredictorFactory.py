from Information_Units.Predictors.MatterSim.MatterSimPredictor import MatterSimPredictor
from Information_Units.Predictors.M3GNet.M3GNetPredictor import M3GNetPredictor
from Information_Units.Predictors.PFP.PFPPredictor import PFPPredictor
from Information_Units.Predictors.DeepMD.DeepMDPredictor import DeepMDPredictor
from Information_Units.Predictors.SynthNN.SynthNNPredictor import SynthNNPredictor
from Information_Units.Predictors.Esen.EsenPredictor import EsenPredictor
from Information_Units.Predictors.MyPred1.MyPred1Predictor import MyPred1Predictor
from Information_Units.Predictors.MyPred2.MyPred2Predictor import MyPred2Predictor

predictor_factory = {
    "mattersim": MatterSimPredictor,
    "m3gnet": M3GNetPredictor,
    "pfp": PFPPredictor,
    "deepmd": DeepMDPredictor,
    "synthnn": SynthNNPredictor,
    "esen": EsenPredictor,
    "mypred1": MyPred1Predictor,
    "mypred2": MyPred2Predictor
}

predictor_registry = {}