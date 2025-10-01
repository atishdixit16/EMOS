from Information_Units.Databases.ICSD.ICSD import ICSD
from Information_Units.Databases.COD.COD import COD
from Information_Units.Databases.OQMD.OQMD import OQMD
from Information_Units.Databases.AFLOWLIB.AFLOWLIB import AFLOWLIB
from Information_Units.Databases.MP.MP import MP
from Information_Units.Databases.Alexandria.Alexandria import Alexandria
from Information_Units.Databases.NOMAD.NOMAD import NOMAD
from Information_Units.Databases.JARVIS.JARVIS import JARVIS

database_factory = {
    "icsd": ICSD,
    "cod": COD,
    "oqmd": OQMD,
    "aflowlib": AFLOWLIB,
    "mp": MP,
    "alexandria": Alexandria,
    "nomad": NOMAD,
    "jarvis": JARVIS
    # Add more when implemented:
}

database_registry = {}