from Information_Units.Generators.MatterGen import MatterGen

generator_factory = {
    "mattergen": MatterGen
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

