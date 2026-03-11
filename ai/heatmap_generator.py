"""
SkyNetics - Heatmap Generator
Generates and updates a probability heatmap mapping GPS coords to fusion scores.
"""
import logging
import json

logger = logging.getLogger(__name__)

class HeatmapGenerator:
    def __init__(self, config: dict):
        self.grid = []
        self.max_prob = 0.0

    def update(self, waypoint: tuple, fusion_result):
        """Map a fusion result to a GPS coordinate."""
        lat, lon = waypoint
        prob = fusion_result.confidence
        
        self.grid.append({
            "lat": lat,
            "lon": lon,
            "probability": prob,
            "sources": fusion_result.sources
        })
        
        if prob > self.max_prob:
            self.max_prob = prob
            logger.info(f"New high-probability zone detected at {lat}, {lon} (Prob: {prob})")

    def save(self, filepath: str):
        """Saves heatmap data to a JSON (or HTML via Folium in production)"""
        with open(filepath.replace('.html', '.json'), 'w') as f:
            json.dump(self.grid, f, indent=4)
        logger.info(f"Saved heatmap data to {filepath.replace('.html', '.json')}")
