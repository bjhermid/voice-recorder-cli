import sounddevice as sd
import numpy as np
import wavio as wv

def record(output_path:str, duration: float, samplerate:int, channels:int, device:int|None):
    data = sd.rec(int(duration*samplerate), samplerate=samplerate, channels=channels, dtype="float32",device=device)
    sd.wait()

    #int16_sample = float_sample×32767 (-32767 s/d 32767 for int16)
    encode_pcm16 = np.int16(np.clip(a=data,a_min=-1.0,a_max=1.0)*3267)
    wv.write(file=output_path,data=encode_pcm16, rate=samplerate,sampwidth=2)


"""
# test
record(
    output_path="recordings/testw0.wav",
    duration=3.0,
    samplerate=44100,
    channels=1,
    device=None
)
"""