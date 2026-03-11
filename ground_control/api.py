"""
SkyNetics - Ground Control API
Provides REST endpoints to interact with the drone in flight.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="SkyNetics Ground Control API")

# Example Global State (in a real app, use Redis or DB)
mission_status = {
    "status": "idle",
    "altitude": 0.0,
    "battery": 100,
    "current_waypoint": [0.0, 0.0]
}

class ZoneData(BaseModel):
    coordinates: list

@app.get("/")
def read_root():
    return {"status": "SkyNetics API is running."}

@app.get("/telemetry")
def get_telemetry():
    return mission_status

@app.post("/mission/start")
def start_mission(zone: ZoneData):
    logger.info(f"Starting mission over zone: {zone.coordinates}")
    mission_status["status"] = "active"
    return {"message": "Mission started"}

@app.post("/mission/rtl")
def return_to_launch():
    logger.info("RTL triggered via API")
    mission_status["status"] = "returning"
    return {"message": "RTL engaged"}

def start_api(host: str = "0.0.0.0", port: int = 8000):
    import uvicorn
    logger.info(f"Starting FastApi on {host}:{port}")
    uvicorn.run(app, host=host, port=port)
