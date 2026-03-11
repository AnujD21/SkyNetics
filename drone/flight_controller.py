"""
SkyNetics - Drone Controller
Handles MAVLink connection and autopilot instructions.
"""
import time
import logging

try:
    from dronekit import connect, VehicleMode, LocationGlobalRelative
except ImportError:
    # Allow simulation/mocking if dronekit isn't installed natively
    pass

logger = logging.getLogger(__name__)

class DroneController:
    def __init__(self, config: dict):
        self.config = config["drone"]
        self.vehicle = None
        self.connected = False

    def connect(self):
        logger.info(f"Connecting to vehicle on: {self.config['connection_string']}")
        try:
            self.vehicle = connect(
                self.config["connection_string"], 
                wait_ready=True, 
                baud=self.config.get("baud_rate", 57600)
            )
            self.connected = True
            logger.info("Drone connected successfully.")
        except Exception as e:
            logger.error(f"Failed to connect to drone: {e}")
            logger.warning("Running in MOCK mode.")

    def arm_and_takeoff(self, target_altitude: float):
        if not self.connected:
            logger.info(f"[MOCK] Arming and taking off to {target_altitude}m")
            return

        logger.info("Basic pre-arm checks")
        while not self.vehicle.is_armable:
            logger.info(" Waiting for vehicle to initialize...")
            time.sleep(1)

        logger.info("Arming motors")
        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True

        while not self.vehicle.armed:
            logger.info(" Waiting for arming...")
            time.sleep(1)

        logger.info(f"Taking off to {target_altitude} meters!")
        self.vehicle.simple_takeoff(target_altitude)

        while True:
            alt = self.vehicle.location.global_relative_frame.alt
            if alt >= target_altitude * 0.95:
                logger.info("Reached target altitude")
                break
            time.sleep(1)

    def goto(self, waypoint: tuple):
        """Navigate to a GPS coordinate (lat, lon)."""
        lat, lon = waypoint
        if not self.connected:
            logger.info(f"[MOCK] Flying to waypoint: {lat}, {lon}")
            time.sleep(0.5)  # Simulate flight time
            return

        target_location = LocationGlobalRelative(lat, lon, self.config["altitude"])
        self.vehicle.simple_goto(target_location, airspeed=self.config["speed"])

        # Basic wait-until-reached logic
        while True:
            current_loc = self.vehicle.location.global_relative_frame
            # Check distance (simplified)
            if abs(current_loc.lat - lat) < 0.0001 and abs(current_loc.lon - lon) < 0.0001:
                break
            time.sleep(1)

    def return_to_launch(self):
        if not self.connected:
            logger.info("[MOCK] Returning to launch (RTL)")
            return
        logger.info("Returning to Launch")
        self.vehicle.mode = VehicleMode("RTL")

    def disconnect(self):
        if self.vehicle:
            self.vehicle.close()
            self.connected = False
            logger.info("Drone connection closed.")
