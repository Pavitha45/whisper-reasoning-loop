import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write


SAMPLE_RATE = 16000
DURATION = 5
OUTPUT_FILE = "layer2_ear/whisper_input.wav"


def capture_audio():
    print("[Layer 2.1] Starting microphone...")
    print(f"[Layer 2.1] Recording for {DURATION} seconds...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    audio = np.squeeze(audio)

    audio_int16 = np.int16(audio * 32767)

    write(
        OUTPUT_FILE,
        SAMPLE_RATE,
        audio_int16
    )

    print("[Layer 2.1] Audio capture successful.")
    print(f"[Layer 2.1] Saved to: {OUTPUT_FILE}")

    return OUTPUT_FILE


if __name__ == "__main__":
    capture_audio()