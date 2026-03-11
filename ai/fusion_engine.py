"""
SkyNetics - AI Sensor Fusion Engine
Combines RF RSSI, Computer Vision, and Thermal data into a unified probability.
"""
import logging

logger = logging.getLogger(__name__)

class FusionResult:
    def __init__(self, confidence: float, sources: dict):
        self.confidence = confidence
        self.sources = sources

class SensorFusionEngine:
    def __init__(self, config: dict):
        self.weights = config["ai"]["fusion_weights"]
        logger.info(f"Initialized Fusion Engine with weights: {self.weights}")

    def fuse(self, rf_data: dict, cv_detections: list, thermal_data: dict) -> FusionResult:
        """
        Fuses data out of the three sensor modalities.
        Returns a uniform probability score (0.0 to 1.0)
        """
        # 1. RF Score (normalize RSSI between -100 and -40)
        rssi = rf_data.get("rssi_dbm", -100)
        rf_score = max(0.0, min(1.0, (rssi + 100) / 60.0))
        
        # 2. CV Score (highest confidence detection)
        cv_score = 0.0
        if cv_detections:
            cv_score = max([d.get("confidence", 0.0) for d in cv_detections])
            
        # 3. Thermal Score (mock logic based on heat gradient)
        thermal_score = thermal_data.get("max_gradient", 0.0) / 10.0
        thermal_score = max(0.0, min(1.0, thermal_score))

        # Apply weights
        total_confidence = (
            rf_score * self.weights.get("rf", 0.33) +
            cv_score * self.weights.get("vision", 0.33) +
            thermal_score * self.weights.get("thermal", 0.33)
        )

        sources = {
            "rf_raw": rssi,
            "cv_raw": cv_score,
            "thermal_raw": thermal_data.get("max_gradient", 0),
            "rf_weighted": rf_score * self.weights.get("rf", 0.33),
            "cv_weighted": cv_score * self.weights.get("vision", 0.33),
            "thermal_weighted": thermal_score * self.weights.get("thermal", 0.33)
        }
        
        return FusionResult(round(total_confidence, 3), sources)
