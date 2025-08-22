import queue
import sys
import soundfile as sf
import sounddevice as sd

# Recording


def record(output: str, duration: float, samplerate: int, channels: int, device: int | None):
    q = queue.Queue()

    def _callback(indata, frames, time, status):
        # stream callback
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

    # open sound file, open inputstream
    with sf.SoundFile(output, mode='w', samplerate=samplerate, channels=channels) as file:
        with sd.InputStream(
            samplerate=samplerate,
            channels=channels,
            device=device,
            callback=_callback,
        ):
            frame_write = int(duration * samplerate)
            written = 0
            while written < frame_write:
                data = q.get()
                remaining = frame_write - written
                print(len(data))
                if remaining < len(data):
                    data = data[:remaining]
                file.write(data)
                written += len(data)


'''
# test
record(
    output="recordings/test0.wav",
    duration=5.0,
    samplerate=44100,
    channels=1,
    device=None
)
'''
