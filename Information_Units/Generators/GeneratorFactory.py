from Information_Units.Generators.MatterGen.MatterGen import MatterGen
from Information_Units.Generators.GNoME.GNoME import GNoME
from Information_Units.Generators.iMatGen.iMatGen import iMatGen
from Information_Units.Generators.MatGAN.MatGAN import MatGAN
from Information_Units.Generators.MolGAN.MolGAN import MolGAN
from Information_Units.Generators.CondDFCVAE.CondDFCVAE import CondDFCVAE
from Information_Units.Generators.MyGen1.MyGen1 import MyGen1
from Information_Units.Generators.MyGen2.MyGen2 import MyGen2

generator_factory = {
    "mattergen": MatterGen,
    "gnome": GNoME,
    "imatgen": iMatGen,
    "matgan": MatGAN,
    "molgan": MolGAN,
    "dfc-vae": CondDFCVAE,
    "mygen1": MyGen1,
    "mygen2": MyGen2
}

generator_registry = {}

