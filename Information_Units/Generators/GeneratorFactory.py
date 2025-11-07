from Information_Units.Generators.MatterGen.MatterGenGenerator import MatterGenGenerator
from Information_Units.Generators.GNoME.GNoMEGenerator import GNoMEGenerator
from Information_Units.Generators.Imatgen.ImatgenGenerator import ImatgenGenerator
from Information_Units.Generators.MatGAN.MatGANGenerator import MatGANGenerator
from Information_Units.Generators.MolGAN.MolGANGenerator import MolGANGenerator
from Information_Units.Generators.Conddfcvae.ConddfcvaeGenerator import ConddfcvaeGenerator
from Information_Units.Generators.MyGen1.MyGen1Generator import MyGen1Generator
from Information_Units.Generators.MyGen2.MyGen2Generator import MyGen2Generator

generator_factory = {
    "mattergen": MatterGenGenerator,
    "gnome": GNoMEGenerator,
    "imatgen": ImatgenGenerator,
    "matgan": MatGANGenerator,
    "molgan": MolGANGenerator,
    "cond_dfc_vae": ConddfcvaeGenerator,
    "mygen1": MyGen1Generator,
    "mygen2": MyGen2Generator
}

generator_registry = {}

