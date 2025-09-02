from Information_Units.Databases.ICSD import ICSD
from Information_Units.Databases.COD import COD

database_factory = {
    "icsd": ICSD,
    "cod": COD
    # Add more when implemented:
}

database_registry = {}