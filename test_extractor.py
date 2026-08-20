import pytest
from pydantic import BaseModel, Field
from typing import Optional, Literal
from extractor import Extractor

class MechanicBrakes(BaseModel):
    axle: Optional[Literal["front", "rear"]] = Field(default=None)
    pad_thickness_mm: Optional[float] = Field(default=None)
    rotor_condition: Optional[str] = Field(default=None)

def test_extractor_full_fields():
    extractor = Extractor(model_path="dummy") # We'll mock the LLM for the test or use a small model
    # Wait, testing an LLM is tricky because it takes time and requires a model file.
    # To avoid downloading a large model during tests, we can mock `create_chat_completion` 
    # of Llama class, testing the Extractor's integration with Pydantic and JSON parsing.
    
    class MockLlama:
        def __init__(self, *args, **kwargs):
            pass
        
        def create_chat_completion(self, messages, response_format):
            # Assert schema was passed
            assert "schema" in response_format
            assert response_format["type"] == "json_object"
            return {
                "choices": [{
                    "message": {
                        "content": '{"axle": "front", "pad_thickness_mm": 5.5, "rotor_condition": "good"}'
                    }
                }]
            }
            
    # Monkeypatch the Llama class inside extractor
    import extractor as ex
    ex.Llama = MockLlama
    
    extractor_instance = ex.Extractor("dummy_path")
    
    text = "The front brakes have 5.5mm of pad left and the rotors are in good condition."
    result = extractor_instance.extract(text=text, schema=MechanicBrakes)
    
    assert isinstance(result, MechanicBrakes)
    assert result.axle == "front"
    assert result.pad_thickness_mm == 5.5
    assert result.rotor_condition == "good"

def test_extractor_missing_fields():
    import extractor as ex
    
    class MockLlamaMissing:
        def __init__(self, *args, **kwargs):
            pass
            
        def create_chat_completion(self, messages, response_format):
            return {
                "choices": [{
                    "message": {
                        "content": '{"axle": "rear"}'
                    }
                }]
            }
            
    ex.Llama = MockLlamaMissing
    extractor_instance = ex.Extractor("dummy_path")
    
    text = "The rear brakes look okay."
    result = extractor_instance.extract(text=text, schema=MechanicBrakes)
    
    assert isinstance(result, MechanicBrakes)
    assert result.axle == "rear"
    assert result.pad_thickness_mm is None
    assert result.rotor_condition is None
