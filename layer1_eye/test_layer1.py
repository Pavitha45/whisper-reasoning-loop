from pathlib import Path
import sys
import cv2

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from layer1_eye.capture import get_frame
from layer1_eye.detect_screen import detect_screen
from layer1_eye.read_vitals import read_screen


BASE_DIR = Path(__file__).resolve().parent
DETECTED_SCREEN = BASE_DIR / "detected_screen.png"


def run_layer1():

    print("=" * 60)
    print("SECURE WHISPER-REASONING LOOP")
    print("LAYER 1 INTEGRATION TEST")
    print("=" * 60)

    # -----------------------------
    # TEST 1: Capture
    # -----------------------------
    print("\n[TEST 1] Capturing monitor frame...")

    captured_image = get_frame()

    if captured_image is None:
        raise RuntimeError(
            "Layer 1.1 capture failed."
        )

    print("[TEST 1] PASS")

    # -----------------------------
    # TEST 2: Screen detection
    # -----------------------------
    print("\n[TEST 2] Detecting screen...")

    screen, coordinates = detect_screen(
        captured_image
    )

    if screen is None:
        raise RuntimeError(
            "Layer 1.2 screen detection failed."
        )

    print("[TEST 2] PASS")

    # Save detected screen
    if not cv2.imwrite(
        str(DETECTED_SCREEN),
        screen
    ):
        raise RuntimeError(
            "Could not save detected screen."
        )

    # -----------------------------
    # TEST 3: OCR + parsing
    # -----------------------------
    print("\n[TEST 3] Reading vital signs...")

    reading = read_screen(
        DETECTED_SCREEN
    )

    # -----------------------------
    # TEST 4: Validate result
    # -----------------------------
    print(
        "\n[TEST 4] Validating "
        "structured vital signs..."
    )

    values = [
        reading.heart_rate,
        reading.spo2,
        reading.blood_pressure_sys,
        reading.blood_pressure_dia,
        reading.resp_rate,
    ]

    if any(value is None for value in values):
        raise RuntimeError(
            "Layer 1 produced incomplete "
            "vital-sign data."
        )

    print("[TEST 4] PASS")

    # -----------------------------
    # FINAL RESULT
    # -----------------------------
    print("\n" + "=" * 60)
    print("LAYER 1 INTEGRATION TEST PASSED")
    print("=" * 60)

    print("\nFinal VitalSignsReading:")
    print(
        f"Heart rate      : "
        f"{reading.heart_rate}"
    )
    print(
        f"SpO2             : "
        f"{reading.spo2}"
    )
    print(
        f"Blood pressure  : "
        f"{reading.blood_pressure_sys}/"
        f"{reading.blood_pressure_dia}"
    )
    print(
        f"Respiratory rate : "
        f"{reading.resp_rate}"
    )


if __name__ == "__main__":
    run_layer1()