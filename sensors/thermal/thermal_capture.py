"""
SkyNetics - Thermal Camera Integration
"""
import logging
import random

logger = logging.getLogger(__name__)

class ThermalCapture:
    def __init__(self, config: dict):
        self.device = config["thermal"].get("device", "lepton")
        logger.info(f"Initialized ThermalCapture for {self.device}")

    def capture(self) -> dict:
        """
        Returns thermal imagery data. 
        Mocked to return a random thermal gradient.
        """
        return {
            "max_gradient": round(random.uniform(0.5, 4.0), 2),
            "frame_avg_temp": 0.5
        }
