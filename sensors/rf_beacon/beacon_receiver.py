"""
SkyNetics - RF Beacon Receiver Module
Handles reading data from the 457 kHz beacon via serial.
"""
import logging
import random
import time

logger = logging.getLogger(__name__)

class RFBeaconReceiver:
    def __init__(self, config: dict):
        self.config = config["rf_beacon"]
        self.connected = False
        
        # In a real run, this would open a pyserial connection here
        logger.info(f"Initialized RF Beacon Receiver on {self.config.get('port')}")

    def read(self) -> dict:
        """
        Reads the latest signal strength from the hardware.
        Returns mocked data for the software prototype phase.
        """
        # Mock payload: simulates reading RSSI (Signal strength)
        # Randomly simulates getting closer to a target
        base_rssi = -90
        noise = random.uniform(-5, 5)
        mock_rssi = base_rssi + noise
        
        # 10% chance of a "strong" signal hit for demo purposes
        if random.random() > 0.9:
            mock_rssi = random.uniform(-65, -40)
            
        return {
            "timestamp": time.time(),
            "frequency": 457000,
            "rssi_dbm": mock_rssi,
            "detected": mock_rssi > self.config.get("rssi_threshold", -80)
        }
