# SkyNetics System Architecture Overview

## 1. High-Level Flow
1. **Mission Planning:** User uploads a GeoJSON zone. Ground Control path-plans a grid.
2. **Flight:** DroneKit executes MAVLink commands asynchronously.
3. **Data Acquisition:** 3 independent sensors trigger at 10Hz/30Hz.
4. **Edge AI:** Core processing runs entirely locally on Jetson Nano. Model inference runs on YOLOv8 Nano via PyTorch/TensorRT.
5. **Fusion:** Weight-based multi-sensor scoring generates a normalized [0,1] confidence score.
6. **Telemetry:** If `confidence > 0.8`, coordinates hit the Ground Control webhook for emergency dispatch.

## 2. Rationale
- **Why 3 sensors?** Thermal fails in sunlight/snow glare. RGB fails at night/under snow. RF requires the victim to have a beacon, which isn't always true. The fusion model compensates for the blind spots of individual sensors.
- **Why Edge compute?** Avalanche zones rarely have 4G/5G cell service. Relying on an AWS backend is a fatal flaw for a search-and-rescue operation.

## 3. Scale Up
For production, the ground control orchestrator would manage **swarms** of drones. The API endpoints in `ground_control/api.py` are stateless to allow scaling to N drones returning telemetry concurrently.
