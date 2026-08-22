from pathlib import Path
import whisper

BASE_DIR = Path(__file__).resolve().parent
AUDIO_FILE = BASE_DIR / "test_audio" / "whisper_test.mp3"


def transcribe_audio(audio_path):
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print("[Layer 2.2] Loading Whisper model...")

    model = whisper.load_model("base")

    print("[Layer 2.2] Transcribing audio...")

    result = model.transcribe(
        str(audio_path),
        fp16=False
    )

    text = result["text"].strip()

    print("\n[Layer 2.2] Transcription result:")
    print(text)

    return text


if __name__ == "__main__":
    transcribe_audio(AUDIO_FILE)