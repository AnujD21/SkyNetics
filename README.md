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

Every year, avalanches and landslides trap victims under meters of debris, ice, and snow. The **golden window of survival** — roughly **15 to 60 minutes** — makes speed of detection the single most important factor in survival outcomes. Traditional rescue operations rely on manual probing, large search teams, or heavy GPR units that are slow, physically exhausting, and often dangerously late in unstable terrain.

**SkyNetics** is a modular, AI-driven autonomous drone platform designed to sweep disaster zones at speed. It fuses data from RGB and thermal sensing modalities, processes it locally on a **Raspberry Pi** edge computer, and transmits GPS coordinates via **LoRa telemetry** to ground rescue teams.

---

## 🎯 Problem Statement

| Challenge | Current Reality |
|---|---|
| **Detection Speed** | Manual probing is incredibly slow; survival drops significantly outside the "Golden Hour". |
| **Harsh Conditions** | Fog, snowfall, and rugged terrain make visual search highly inefficient and dangerous. |
| **Rescue Team Risk** | Further avalanches or landslides during searches endanger rescue personnel. |
| **Network Infrastructure** | Extreme remote terrain makes cloud-dependent AI systems useless. |

**SkyNetics** addresses these challenges using autonomous navigation (**iNav**), multi-sensor AI fusion (**Vision + Thermal**), and onboard edge computing (**Raspberry Pi**), entirely bypassing the need for cloud infrastructure.

---

## 🔬 Solution Architecture

### Multi-Sensor Detection Suite

The drone utilizes a multi-sensor detection approach, processing outputs via a fusion pipeline:

```
┌─────────────────────────────────────────────────────────┐
│                   SkyNetics Drone                       │
│                                                         │
│        ┌──────────────┐         ┌─────────────┐         │
│        │ RGB Camera   │         │  Thermal    │         │
│        │ + YOLOv8n    │         │  Imaging    │         │
│        │ (CV Model)   │         │  Module     │         │
│        └──────┬───────┘         └──────┬──────┘         │
│               │                        │                │
│               └───────────┬────────────┘                │
│                           ▼                             │
│              ┌─────────────────────────┐                │
│              │  Multi-Sensor Fusion AI │                │
│              │     (Raspberry Pi)      │                │
│              └────────────┬────────────┘                │
│                           │                             │
│              ┌────────────▼────────────┐                │
│              │   Victim Localization   │                │
│              │   + GPS Coordinates     │                │
│              └────────────┬────────────┘                │
└───────────────────────────┼─────────────────────────────┘
                            │ Telemetry Link (433 MHz LoRa)
                            ▼
                  ┌─────────────────┐
                  │ Ground Control  │
                  │ Station / App   │
                  └─────────────────┘
```

### 1. 📷 Computer Vision Module (YOLOv8n)
- Real-time human detection from aerial imagery using YOLO.
- Identifies visual indicators: human body parts, clothing, or equipment visible on the snow or debris surface.

### 2. 🌡️ Thermal Imaging Module
- Detects heat signatures indicating human presence beneath shallow snow layers or landslide debris.
- Effective under low visibility, fog, and nighttime conditions, filtering environmental noise.

### 3. 🧠 Edge Computing (Raspberry Pi)
- All AI inference and fusion algorithms run **onboard**. No cloud connectivity is required.
- Sensor outputs are fused to identify targets, drastically reducing false positives.

### 4. 🚁 Autonomous Navigation (iNav) & Telemetry
- The drone autonomously scans zones using pre-programmed lawnmower search paths via **iNav firmware**.
- Telemetry and critical alerts (GPS positions) are sent to the ground over long-range **433 MHz LoRa**.
- Live video streams via a **5.8 GHz VTX** to mobile devices.
- Optionally deploys payloads (e.g., small medical supplies) over high-confidence detection spots.

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
