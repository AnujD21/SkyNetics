"""
SkyNetics - RGB Camera Capture Module
"""
import logging
import cv2

logger = logging.getLogger(__name__)

class CameraCapture:
    def __init__(self, config: dict):
        self.camera_id = config["camera"].get("device_id", 0)
        # self.cap = cv2.VideoCapture(self.camera_id)
        logger.info(f"Initialized CameraCapture on device {self.camera_id}")

    def capture(self):
        """Returns the latest RGB frame."""
        # if not self.cap.isOpened():
        #     return None
        # ret, frame = self.cap.read()
        # return frame if ret else None
        
        # MOCK: Return a blank array for prototype purposes
        return None

    def release(self):
        # self.cap.release()
        pass
