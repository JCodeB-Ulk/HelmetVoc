import sounddevice as sd
import numpy as np
from scipy.signal import butter, sosfilt, sosfilt_zi

fs = 44100

sos = butter(
    4,
    [700 / (fs / 2), 3200 / (fs / 2)],
    btype='band',
    output='sos'
)

zi = sosfilt_zi(sos)

state = None


def callback(indata, outdata, frames, time, status):
    global zi, state

    audio = indata[:, 0].astype(np.float32)

    audio, zi = sosfilt(sos, audio, zi=zi)
    audio = np.tanh(audio * 1.5)

    if state and not state.is_talking:
        audio[:] = 0

    outdata[:, 0] = audio


def start_stream(shared_state):
    global state
    state = shared_state

    print("Starting audio stream...")

    stream = sd.Stream(
        samplerate=fs,
        channels=1,
        blocksize=2048,
        latency='low',
        callback=callback
    )

    stream.start()
    return stream