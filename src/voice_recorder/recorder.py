from voice_recorder.backend import soundfile_back, wavio_back, scipy_back
import sounddevice as sd

BACKENDS = {
    "soundfile": soundfile_back.record,
    "wavio": wavio_back.record,
    "scipy": scipy_back.record,
}


def list_devices():
    devices = sd.query_devices()
    res = []

    for _id, dev in enumerate(devices):
        if dev.get("max_input_channels", 0) > 0:
            res.append(
                {
                    "id": _id,
                    "name": dev.get("name", f"Device {_id}"),
                    "channels": dev.get("max_input_channels", 0),
                    "default_samplerate": dev.get("default_samplerate", 44100),
                }
            )

    return res


def record_wav(
    output_path: str,
    duration: float,
    samplerate: int = 44100,
    channels: int = 1,
    device: int | None = None,
    backend: str = "soundfile",
):
    if backend not in BACKENDS:
        raise ValueError(f"Unsupported Backend : {backend}")
    BACKENDS[backend](output_path, duration, samplerate, channels, device)
