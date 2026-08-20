from faster_whisper import WhisperModel
import os

class STT:
    def __init__(self, model_size="tiny"):
        # CPU for prototype unless GPU is explicitly configured, but faster-whisper will use GPU if available.
        # "tiny" model is fast enough for verifying the pipeline.
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")

    def transcribe(self, audio_path: str) -> str:
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        segments, info = self.model.transcribe(audio_path, beam_size=5)
        text = " ".join([segment.text for segment in segments])
        return text.strip()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        stt = STT()
        print(stt.transcribe(sys.argv[1]))
    else:
        print("Usage: python stt.py <audio_file>")
