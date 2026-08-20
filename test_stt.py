import os
import pytest
from stt import STT

def test_stt_transcribe_returns_string():
    # Arrange
    stt = STT(model_size="tiny")
    test_audio_path = "test.wav"
    
    # Ensure test.wav exists
    assert os.path.exists(test_audio_path), "test.wav must exist for this test"
    
    # Act
    result = stt.transcribe(test_audio_path)
    
    # Assert
    assert isinstance(result, str)
    # The sine wave might transcribe to empty string or some random hallucinated noise,
    # but the method should return a string without crashing.
