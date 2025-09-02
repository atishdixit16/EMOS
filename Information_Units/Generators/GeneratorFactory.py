from Information_Units.Generators.MatterGen import MatterGenGenerator

generator_factory = {
    "mattergen": MatterGenGenerator
    # Add more when implemented:
    # "gnome": GNoMEGenerator,
    # "imatgen": IMatGenGenerator,
    # "matgan": MatGANGenerator,
    # "molgan": MolGANGenerator,
    # "dfc-vae": CondDFCVAEGenerator,
    # "mygen1": MyGen1Generator,
    # "mygen2": MyGen2Generator,
}

generator_registry = {}

