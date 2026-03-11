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
                "vision": 0.60,
                "thermal": 0.40
            }
        }
    }
    return SensorFusionEngine(config)

def test_fusion_high_confidence(engine):
    cv_dets = [{"confidence": 0.95}] # Very high confidence vision
    therm_data = {"max_gradient": 9.0} # Intense thermal hit

    result = engine.fuse(cv_dets, therm_data)
    
    # We expect a high confidence result from these strong inputs
    # 0.95 * 0.60 + 0.9 * 0.40 = 0.57 + 0.36 = 0.93
    assert result.confidence > 0.85
    assert "cv_raw" in result.sources
    assert "thermal_raw" in result.sources

def test_fusion_low_confidence(engine):
    cv_dets = [] # No vision
    therm_data = {"max_gradient": 0.2} # Weak thermal hit

    result = engine.fuse(cv_dets, therm_data)
    
    # We expect a very low score
    # 0.0 * 0.60 + 0.02 * 0.40 = 0.008
    assert result.confidence < 0.10
