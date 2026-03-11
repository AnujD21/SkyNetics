"""
SkyNetics - Alert System
Dispatches high-confidence victim detections.
"""
import logging
import requests

logger = logging.getLogger(__name__)

class AlertSystem:
    def __init__(self, config: dict):
        self.webhook_url = config["ground_control"].get("alert_webhook_url", "")

    def dispatch(self, waypoint: tuple, fusion_data):
        """Send an alert to operators with GPS coordinates."""
        lat, lon = waypoint
        prob = fusion_data.confidence
        
        msg = f"🚨 URGENT: High probability victim detection! 🚨\n" \
              f"Probability: {prob * 100}%\n" \
              f"Coordinates: {lat}, {lon}\n" \
              f"Open Map: https://www.google.com/maps?q={lat},{lon}\n" \
              f"Sensor Sources: {fusion_data.sources}"
              
        logger.warning(f"\n{'-'*60}\n{msg}\n{'-'*60}")
        
        # Send Webhook if configured
        if self.webhook_url:
            try:
                requests.post(self.webhook_url, json={"text": msg})
                logger.debug("Alert webhook fired successfully.")
            except Exception as e:
                logger.error(f"Failed to fire alert webhook: {e}")
