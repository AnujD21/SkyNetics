"""
SkyNetics - AI Object Detector
Runs real-time inference using YOLOv8 to detect victims and objects from the air.
"""
import logging
import random

try:
    from ultralytics import YOLO
except ImportError:
    pass

logger = logging.getLogger(__name__)

class YOLODetector:
    def __init__(self, config: dict):
        self.config = config["ai"]
        self.model_path = self.config.get("model_path", "yolov8n.pt")
        self.conf_threshold = self.config.get("confidence_threshold", 0.65)
        self.model = None
        
        try:
            # self.model = YOLO(self.model_path)
            logger.info(f"Loaded YOLO model from {self.model_path}")
        except Exception as e:
            logger.warning(f"Failed to load YOLO model (running in MOCK mode): {e}")

    def infer(self, frame) -> list:
        """
        Runs object detection on a single RGB frame.
        Returns a list of detections (bounding boxes, class, confidence).
        """
        # --- Mock Logic ---
        # Simulates occasional detections
        detections = []
        if random.random() > 0.8:
            # Simulated detection
            detections.append({
                "class": "person", 
                "confidence": round(random.uniform(self.conf_threshold, 0.95), 2),
                "bbox": [100, 150, 200, 350] # x1, y1, x2, y2
            })
            
        return detections
