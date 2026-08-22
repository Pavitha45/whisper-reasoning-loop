from pathlib import Path
import sys
import easyocr

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from layer1_eye.parse_vitals import parse_vitals


BASE_DIR = Path(__file__).resolve().parent
INPUT_IMAGE = BASE_DIR / "detected_screen.png"


def read_screen(image_path):
    if not image_path.exists():
        raise FileNotFoundError(
            f"Screen image not found: {image_path}"
        )

    print("[Layer 1.3] Starting EasyOCR...")

    reader = easyocr.Reader(
        ["en"],
        gpu=False
    )

    results = reader.readtext(str(image_path))

    print(
        f"[Layer 1.3] OCR detected "
        f"{len(results)} text regions."
    )

    for result in results:
        bounding_box, text, confidence = result

        print(
            f"Text: {text!r} | "
            f"Confidence: {confidence:.2f}"
        )

    # Send OCR results to the parser
    reading = parse_vitals(results)

    print("\n[Layer 1.3] Parsed vital signs:")
    print(f"Heart rate: {reading.heart_rate}")
    print(f"SpO2: {reading.spo2}")
    print(
        f"Blood pressure: "
        f"{reading.blood_pressure_sys}/"
        f"{reading.blood_pressure_dia}"
    )
    print(f"Respiratory rate: {reading.resp_rate}")

    return reading


if __name__ == "__main__":
    read_screen(INPUT_IMAGE)