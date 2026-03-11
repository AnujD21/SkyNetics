"""
SkyNetics - Mission Simulation Script
Runs an end-to-end mock mission without hardware connected.
"""
import argparse
import time
import logging
import random
from pathlib import Path
import sys

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

# Mocked imports to skip hardware requirements
from drone.waypoint_generator import generate_lawnmower_path
from ai.fusion_engine import SensorFusionEngine
from ai.heatmap_generator import HeatmapGenerator
from ground_control.alert_system import AlertSystem
import yaml

def load_config(config_path: str = "config.yaml") -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def run_simulation(zone_file: str):
    config = load_config()
    
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Initializing SkyNetics SIMULATION Mode")
    
    waypoints = generate_lawnmower_path(zone_file, config)
    fusion = SensorFusionEngine(config)
    heatmap = HeatmapGenerator(config)
    alerts = AlertSystem(config)

    logger.info("Drone taking off to 15m")
    time.sleep(1.5)

    for i, wp in enumerate(waypoints):
        logger.info(f"Navigating to WP {i+1}/{len(waypoints)}: {wp}")
        time.sleep(0.5)  # Simulate flight time

        # Mock sensor data
        cv_dets = []
        therm_data = {"max_gradient": random.uniform(0.1, 1.5)}

        # Force a strong hit on waypoint 7 for demonstration
        if i == 7:
            cv_dets = [{"class": "person", "confidence": 0.88, "bbox": [0,0,10,10]}]
            therm_data["max_gradient"] = 3.5

        result = fusion.fuse(cv_dets, therm_data)
        heatmap.update(wp, result)

        if result.confidence >= config["ai"]["detection_confidence_alert"]:
            alerts.dispatch(wp, result)

    logger.info("Mission Complete. Returning to launch.")
    time.sleep(1.5)
    
    heatmap.save("mission/output_heatmap.html")
    logger.info("Drone landed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--zone", type=str, required=True, help="GeoJSON zone file")
    args = parser.parse_args()
    
    # Ensure mission dir exists
    Path("mission").mkdir(exist_ok=True)
    
    run_simulation(args.zone)
