import wave
import struct
import math

def create_test_wav(filename):
    # generate a sine wave for testing
    sample_rate = 16000
    duration = 1
    num_samples = sample_rate * duration
    with wave.open(filename, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        for i in range(num_samples):
            value = int(32767.0 * math.cos(2 * math.pi * 440.0 * i / sample_rate))
            data = struct.pack('<h', value)
            f.writeframesraw(data)

create_test_wav('test.wav')
