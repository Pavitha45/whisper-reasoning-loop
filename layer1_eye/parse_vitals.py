import re
from datetime import datetime

from shared.schema import VitalSignsReading


def parse_vitals(ocr_results):
    """
    Convert raw EasyOCR results into a VitalSignsReading.
    """

    texts = [result[1] for result in ocr_results]

    combined_text = " ".join(texts)

    # Normalize common OCR mistakes
    normalized = combined_text.upper()

    normalized = normalized.replace("PATE", "RATE")
    normalized = normalized.replace("BLCOD", "BLOOD")
    normalized = normalized.replace("PESP", "RESP")
    normalized = normalized.replace(",", "/")
    normalized = normalized.replace(".", " ")

    # Heart rate
    hr_match = re.search(
        r"HEART\s+RATE\s*[:\-]?\s*(\d{2,3})",
        normalized
    )

    # SpO2
    spo2_match = re.search(
        r"SPO2\s*[:\-]?\s*(\d{2,3})",
        normalized
    )

    # Blood pressure
    bp_match = re.search(
        r"BLOOD\s+PRESSURE\s*[:\-]?\s*(\d{2,3})\s*/\s*(\d{2,3})",
        normalized
    )

    # Respiratory rate
    rr_match = re.search(
        r"RESP\s+RATE\s*[:\-]?\s*(\d{1,3})",
        normalized
    )

    heart_rate = float(hr_match.group(1)) if hr_match else None
    spo2 = float(spo2_match.group(1)) if spo2_match else None

    bp_sys = (
        float(bp_match.group(1))
        if bp_match else None
    )

    bp_dia = (
        float(bp_match.group(2))
        if bp_match else None
    )

    resp_rate = (
        float(rr_match.group(1))
        if rr_match else None
    )

    # Basic validation
    if heart_rate is not None and not 30 <= heart_rate <= 220:
        heart_rate = None

    if spo2 is not None and not 50 <= spo2 <= 100:
        spo2 = None

    if bp_sys is not None and not 50 <= bp_sys <= 250:
        bp_sys = None

    if bp_dia is not None and not 30 <= bp_dia <= 150:
        bp_dia = None

    if resp_rate is not None and not 5 <= resp_rate <= 80:
        resp_rate = None

    reading = VitalSignsReading(
        heart_rate=heart_rate,
        spo2=spo2,
        blood_pressure_sys=bp_sys,
        blood_pressure_dia=bp_dia,
        resp_rate=resp_rate,
        timestamp=datetime.now(),
        source_confidence=0.0,
    )

    return reading