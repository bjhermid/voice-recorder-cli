import sounddevice as sd
import numpy as np
from scipy.io import wavfile


def record(
    output_path: str,
    duration: float,
    samplerate: int,
    channels: int,
    device: int | None,
):
    data = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=channels,
        dtype="float32",
        device=device,
    )
    sd.wait()

    # int16_sample = float_sample×32767 (-32767 s/d 32767 for int16)
    encode_int16 = np.int16(np.clip(a=data, a_min=-1.0, a_max=1.0) * 32767)
    wavfile.write(output_path, rate=samplerate, data=encode_int16)
