# SkyNetics System Architecture Overview

## 1. High-Level Flow
1. **Mission Planning:** User uploads a GeoJSON zone. Ground Control path-plans a grid.
2. **Flight:** The drone navigation is handled autonomously using **iNav** flight firmware.
3. **Data Acquisition:** 2 independent sensors (RGB Camera and Thermal Imager) trigger at 10Hz/30Hz.
4. **Edge AI:** Core computing runs entirely locally on a **Raspberry Pi**. Model inference runs on YOLOv8 Nano.
5. **Fusion:** Weight-based multi-sensor scoring generates a normalized [0,1] confidence score from visual and thermal hits.
6. **Telemetry:** If `confidence > 0.8`, GPS coordinates are transmitted instantly via **433 MHz LoRa** to the Ground Control station for emergency dispatch, while **5.8 GHz VTX** streams live aerial footage to smart devices.
7. **Payload Delivery:** Can support airdropping small medical supplies to the detected location.

## 2. Rationale
- **Why 2 sensors?** The fusion model compensates for the blind spots of individual sensors. Thermal helps detect body heat in low visibility or buried under debris, while RGB vision identifies clothing or equipment on the surface.
- **Why Edge compute?** Avalanche and landslide zones rarely have cellular service. Processing data on the drone via the Raspberry Pi eliminates cloud dependency, making it a reliable solution for search-and-rescue.
- **Why iNav and LoRa?** iNav provides excellent waypoint navigation features, and LoRa ensures long-range communication in mountainous terrain where standard radios fail.

## 3. Scale Up
For production, the ground control orchestrator would manage **swarms** of drones. The API endpoints in `ground_control/api.py` are stateless to allow scaling to N drones returning telemetry concurrently.
