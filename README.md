# 🚁 SkyNetics — AI-Powered Drone System for Avalanche and Landslide Victim Detection

<div align="center">

![SkyNetics Banner](https://img.shields.io/badge/SkyNetics-Avalanche_Landslide_AI-blue?style=for-the-badge&logo=drone&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3670A0?style=flat-square&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/YOLO-v8%20Nano-00FFFF?style=flat-square)](https://ultralytics.com/)
[![Raspberry Pi](https://img.shields.io/badge/Edge%20AI-Raspberry%20Pi-C51A4A?style=flat-square&logo=raspberry-pi)](https://www.raspberrypi.org/)
[![Status](https://img.shields.io/badge/Status-Hackathon%20Prototype-orange?style=flat-square)]()

> **"Every second counts. We make sure no one is left behind."**  
> An autonomous, AI-powered drone platform that detects avalanche and landslide victims rapidly and accurately — where traditional search methods fail.

[📖 Overview](#-overview) · [🎯 Problem Statement](#-problem-statement) · [🔬 Solution Architecture](#-solution-architecture) · [⚙️ Tech Stack](#️-tech-stack) · [🗂️ Repo Structure](#️-repo-structure) · [🚀 Getting Started](#-getting-started) · [📊 Results](#-results) · [🗺️ Roadmap](#️-roadmap)

</div>

---

## 📖 Overview

The proposed system is an AI-powered autonomous drone platform designed to rapidly detect victims buried under avalanches or landslides, where survival depends heavily on the limited rescue window known as the Golden Hour. Traditional search methods rely on manual probing and ground teams, which are slow, dangerous, and inefficient across large disaster areas. The system addresses these challenges by combining autonomous drone navigation, AI-based detection, and multi-sensor fusion to accelerate victim localization and support rescue teams.

---

## 🎯 Problem Statement

| Challenge | Current Reality |
|---|---|
| **Detection Speed** | Manual probing is incredibly slow; survival drops significantly outside the "Golden Hour". |
| **Harsh Conditions** | Fog, snowfall, and rugged terrain make visual search highly inefficient and dangerous. |
| **Rescue Team Risk** | Further avalanches or landslides during searches endanger rescue personnel. |
| **Network Infrastructure** | Extreme remote terrain makes cloud-dependent AI systems useless. |

**SkyNetics** addresses these challenges using autonomous navigation (**iNav** with **optical flow stabilization**), multi-sensor AI fusion (**Vision, Thermal, and mmWave**), and onboard edge computing (**Raspberry Pi**), entirely bypassing the need for cloud infrastructure.

By combining AI-based computer vision, thermal sensing, mmWave life-sign detection, optical flow stabilization, and edge computing, the system significantly reduces search time, improves detection accuracy, and enhances the safety of rescue operations. This integrated approach provides a scalable and cost-effective solution for modern disaster response in avalanche and landslide environments.

---

## 🔬 Solution Architecture

### Multi-Sensor Detection Suite

The drone integrates a multi-sensor detection suite consisting of an RGB camera, thermal imaging module, mmWave radar sensor, and RF beacon detection. All sensor data is processed onboard using a Raspberry Pi edge computing unit. 

```
┌────────────────────────────────────────────────────────────────────────┐
│                          SkyNetics Drone                               │
│                                                                        │
│    ┌──────────────┐     ┌─────────────┐     ┌───────────────────┐      │
│    │ RGB Camera   │     │  Thermal    │     │  mmWave Radar     │      │
│    │ + YOLOv8     │     │  Imaging    │     │  (Micro-movement) │      │
│    └──────┬───────┘     └──────┬──────┘     └─────────┬─────────┘      │
│           │                    │                      │                │
│           └────────────────────┼──────────────────────┘                │
│                                ▼                                       │
│                   ┌─────────────────────────┐                          │
│                   │  Multi-Sensor Fusion AI │                          │
│                   │     (Raspberry Pi)      │                          │
│                   └────────────┬────────────┘                          │
│                                │                                       │
│                   ┌────────────▼────────────┐                          │
│                   │   Victim Localization   │                          │
│                   │   + GPS Coordinates     │                          │
│                   └────────────┬────────────┘                          │
└────────────────────────────────┼───────────────────────────────────────┘
                                 │ Telemetry Link (433 MHz LoRa)
                                 ▼
                     ┌───────────────────────┐
                     │ Ground Control        │
                     │ Station / App         │
                     └───────────────────────┘
```

### 1. 📷 Computer Vision Module (YOLOv8)
- A YOLO-based deep learning model (Ultralytics) processes aerial images in real time to identify visual indicators such as exposed body parts, clothing, or mountaineering equipment.

### 2. 🌡️ Thermal Imaging Module
- A thermal imaging sensor detects heat signatures from victims buried under shallow snow or debris, particularly useful in low-visibility conditions.

### 3. 📡 mmWave Radar Sensor
- A mmWave radar sensor is integrated to identify micro-movements such as breathing or slight body motion beneath snow or debris layers, allowing detection even when victims are not visually visible.

### 4. 🧠 Edge Computing & Fusion (Raspberry Pi)
- All sensor data is processed onboard using a Raspberry Pi edge computing unit, enabling real-time inference without cloud connectivity, which is critical for remote mountainous regions.
- The outputs from the vision model, thermal sensor, and mmWave radar are combined using a multi-sensor fusion algorithm that evaluates detection confidence and generates a probability-based victim location map.

### 5. 🚁 Autonomous Navigation (iNav) & Telemetry
- For stable navigation and precise low-altitude flight in harsh terrain, the drone incorporates an **optical flow sensor**, which measures ground motion using visual pattern tracking. This enables accurate position estimation, drift correction, and stable hovering, especially in GPS-degraded environments such as snow-covered valleys or mountainous regions.
- The drone operates using open-source iNav flight firmware, with the ESC and flight controller configured as a stacked architecture for reliability and modularity. The system supports ~30 minutes of flight endurance and includes payload capability for sensors and emergency airdrops.
- Communication with ground teams is achieved using 433 MHz LoRa-based long-range telemetry, while a 5.8 GHz video transmission system (VTX) streams live aerial footage to rescue teams on smart devices.
- During operation, the drone autonomously scans the disaster zone using a predefined grid-based search pattern, processes sensor data in real time, and transmits GPS coordinates of detected victims to rescue teams for rapid response.

---

## ⚙️ Tech Stack

### Hardware
| Component | Specification |
|---|---|
| **Flight Controller** | iNav compatible Stack (FC + ESC) |
| **Edge Compute** | Raspberry Pi 4 / 5 |
| **Camera** | RGB HD camera (1080p) |
| **Thermal Camera** | FLIR Lepton 3.5 / MLX90640 |
| **Telemetry / VTX** | 433 MHz LoRa / 5.8 GHz VTX |
| **Payload Delivery** | Servo-based airdrop release mechanism |

### Software & AI
| Technology | Purpose |
|---|---|
| **Python 3.10** | Core application logic |
| **YOLOv8 Nano** | Deep learning human detection |
| **OpenCV** | Image processing and frame handling |
| **iNav Configurator** | Flight planning & firmare settings |
| **LoRa Interface** | Serial data transmission via 433MHz |

---

## 🗂️ Repo Structure

```
SkyNetics/
│
├── 📁 drone/                          # iNav interface & drone hardware configuration
├── 📁 sensors/                        # Sensor interfaces (CV and Thermal)
├── 📁 ai/                             # YOLO models & sensor fusion algorithms
├── 📁 ground_control/                 # Ground Station & alert dispatch
├── 📁 training/                       # YOLO model fine-tuning pipeline
├── 📁 tests/                          # Unit and integration tests
├── 📁 scripts/                        # Setup and simulation tools
├── config.yaml                        # Mission parameters and system configs
├── main.py                            # Mission Orchestrator
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Raspberry Pi (running Raspberry Pi OS / Ubuntu)
- Thermal module & RGB Camera

### Installation

```bash
git clone https://github.com/your-org/SkyNetics.git
cd SkyNetics

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Hardware setup script
chmod +x scripts/setup_raspberrypi.sh
./scripts/setup_raspberrypi.sh
```

### Run a Mission

```bash
# Simulate a mission
python main.py --mode simulate --zone sample_data/zone_polygon.json

# Live mission
python main.py --mode live --zone mission/zone.json
```

---

## 📄 License
This project is licensed under the **MIT License**.

---

<div align="center">
**Built with ❤️ for disaster response.**
</div>
