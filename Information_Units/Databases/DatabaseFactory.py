from Information_Units.Databases.ICSD.ICSDDatabase import ICSDDatabase
from Information_Units.Databases.COD.CODDatabase import CODDatabase
from Information_Units.Databases.OQMD.OQMDDatabase import OQMDDatabase
from Information_Units.Databases.AFLOWLIB.AFLOWLIBDatabase import AFLOWLIBDatabase
from Information_Units.Databases.MaterialsProject.MaterialsProjectDatabase import MaterialsProjectDatabase
from Information_Units.Databases.Alexandria.AlexandriaDatabase import AlexandriaDatabase
from Information_Units.Databases.NOMAD.NOMADDatabase import NOMADDatabase
from Information_Units.Databases.JARVIS.JARVISDatabase import JARVISDatabase

database_factory = {
    "icsd": ICSDDatabase,
    "cod": CODDatabase,
    "oqmd": OQMDDatabase,
    "aflowlib": AFLOWLIBDatabase,
    "materials_project": MaterialsProjectDatabase,
    "alexandria": AlexandriaDatabase,
    "nomad": NOMADDatabase,
    "jarvis": JARVISDatabase
}

database_registry = {}