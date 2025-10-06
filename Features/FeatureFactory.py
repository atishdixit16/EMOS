# Import all feature classes
from Features.Materials_Exploration.Material_Search.MaterialSearchFeature import MaterialSearchFeature
from Features.Materials_Exploration.Material_Generation.MaterialGenerationFeature import MaterialGenerationFeature
from Features.Materials_Exploration.Database_Extractor.DatabaseExtractorFeature import DatabaseExtractorFeature
from Features.Materials_Exploration.Material_Characterization.MaterialCharacterizationFeature import MaterialCharacterizationFeature
from Features.Materials_Exploration.DFT_Calculation.DFTCalculationFeature import DFTCalculationFeature
from Features.Materials_Exploration.Crystallographic_Analysis.CrystallographicAnalysisFeature import CrystallographicAnalysisFeature
from Features.Materials_Exploration.Quantum_Mechanics.QuantumMechanicsFeature import QuantumMechanicsFeature
from Features.Materials_Exploration.Tensor_Analysis.TensorAnalysisFeature import TensorAnalysisFeature

from Features.Electronics_Application.Device_Synthesizability.DeviceSynthesizabilityFeature import DeviceSynthesizabilityFeature
from Features.Electronics_Application.Interface_Calculation.InterfaceCalculationFeature import InterfaceCalculationFeature
from Features.Electronics_Application.Property_Prediction.PropertyPredictionFeature import PropertyPredictionFeature
from Features.Electronics_Application.Band_Structure.BandStructureFeature import BandStructureFeature
from Features.Electronics_Application.Thermal_Management.ThermalManagementFeature import ThermalManagementFeature
from Features.Electronics_Application.Reliability_Assessment.ReliabilityAssessmentFeature import ReliabilityAssessmentFeature
from Features.Electronics_Application.Process_Integration.ProcessIntegrationFeature import ProcessIntegrationFeature
from Features.Electronics_Application.Advanced_Characterization.AdvancedCharacterizationFeature import AdvancedCharacterizationFeature


# Feature registry - simple mapping like Information Units
feature_factory = {
    "1": MaterialSearchFeature,
    "2": MaterialGenerationFeature,
    "3": DatabaseExtractorFeature,
    "4": MaterialCharacterizationFeature,
    "5": DFTCalculationFeature,
    "6": CrystallographicAnalysisFeature,
    "7": QuantumMechanicsFeature,
    "8": TensorAnalysisFeature,
    "9": DeviceSynthesizabilityFeature,
    "10": InterfaceCalculationFeature,
    "11": PropertyPredictionFeature,
    "12": BandStructureFeature,
    "13": ThermalManagementFeature,
    "14": ReliabilityAssessmentFeature,
    "15": ProcessIntegrationFeature,
    "16": AdvancedCharacterizationFeature,
}


def create_feature(feature_id, logger=None):
    """Create a feature instance by ID - simple like Information Units"""
    if feature_id not in feature_factory:
        raise ValueError(f"Feature {feature_id} not found in factory")
    
    feature_class = feature_factory[feature_id]
    return feature_class(logger)


def get_available_features():
    """Get list of available feature IDs"""
    return list(feature_factory.keys())


def get_feature_info(feature_id):
    """Get info about a specific feature"""
    if feature_id not in feature_factory:
        return None
    
    feature_class = feature_factory[feature_id]
    # Create temporary instance to get info
    temp_feature = feature_class()
    return temp_feature.info()