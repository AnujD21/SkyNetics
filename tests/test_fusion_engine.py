import pytest
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from ai.fusion_engine import SensorFusionEngine

@pytest.fixture
def engine():
    config = {
        "ai": {
            "fusion_weights": {
                "rf": 0.40,
                "vision": 0.35,
                "thermal": 0.25
            }
        }
    }
    return SensorFusionEngine(config)

def test_fusion_high_confidence(engine):
    rf_data = {"rssi_dbm": -40}  # Very strong signal
    cv_dets = [{"confidence": 0.95}] # Very high confidence vision
    therm_data = {"max_gradient": 9.0} # Intense thermal hit

    result = engine.fuse(rf_data, cv_dets, therm_data)
    
    # We expect a high confidence result from these strong inputs
    assert result.confidence > 0.85
    assert "rf_raw" in result.sources

def test_fusion_low_confidence(engine):
    rf_data = {"rssi_dbm": -95}  # Weak signal
    cv_dets = [] # No vision
    therm_data = {"max_gradient": 0.2} # Weak thermal hit

    result = engine.fuse(rf_data, cv_dets, therm_data)
    
    # We expect a very low score
    assert result.confidence < 0.20
