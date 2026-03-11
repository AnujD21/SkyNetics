"""
SkyNetics - Waypoint Generator
Generates a lawnmower grid search pattern from a GeoJSON polygon.
"""
import json
import logging
import math

logger = logging.getLogger(__name__)

def haversine_offset(lat: float, lon: float, offset_n_m: float, offset_e_m: float):
    """Offset a GPS coordinate by meters North/East."""
    R = 6378137  # Earth radius in meters
    dlat = offset_n_m / R
    dlon = offset_e_m / (R * math.cos(math.pi * lat / 180))
    return lat + (dlat * 180 / math.pi), lon + (dlon * 180 / math.pi)

def generate_lawnmower_path(zone_file: str, config: dict) -> list:
    """Read a JSON boundary and generate search grid (simplified for hackathon)."""
    try:
        with open(zone_file, 'r') as f:
            zone = json.load(f)
    except FileNotFoundError:
        logger.error(f"Cannot find zone file {zone_file}")
        return []

    # In a real app, this parses a polygon and calculates grid lines.
    # For this prototype/mock, we generate a synthetic grid based on the first point.
    spacing = config["mission"]["grid_spacing"]
    start_point = zone.get("features", [{}])[0].get("geometry", {}).get("coordinates", [[[0,0]]])[0][0]
    start_lon, start_lat = start_point

    logger.info(f"Generating lawnmower pattern starting at {start_lat}, {start_lon} with {spacing}m spacing")
    
    waypoints = []
    rows = 5
    cols = 5
    
    for row in range(rows):
        for col in range(cols):
            # Alternate direction for lawnmower sweep
            c = col if row % 2 == 0 else (cols - 1 - col)
            wp = haversine_offset(start_lat, start_lon, row * spacing, c * spacing)
            waypoints.append(wp)
            
    return waypoints
