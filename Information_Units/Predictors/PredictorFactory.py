from Information_Units.Predictors.MatterSim.MatterSim import MatterSim
from Information_Units.Predictors.M3GNet.M3GNet import M3GNet
from Information_Units.Predictors.PFP.PFP import PFP
from Information_Units.Predictors.DeepMD.DeepMD import DeepMD
from Information_Units.Predictors.SynthNN.SynthNN import SynthNN
from Information_Units.Predictors.eSEN.eSEN import eSEN
from Information_Units.Predictors.MyPred1.MyPred1 import MyPred1
from Information_Units.Predictors.MyPred2.MyPred2 import MyPred2

predictor_factory = {
    "mattersim": MatterSim,
    "m3gnet": M3GNet,
    "pfp": PFP,
    "deepmd": DeepMD,
    "synthnn": SynthNN,
    "esen": eSEN,
    "mypred1": MyPred1,
    "mypred2": MyPred2
}

predictor_registry = {}