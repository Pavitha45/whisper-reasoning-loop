from shared.schema import VitalSignsReading


def assess_confidence(vitals: VitalSignsReading) -> dict:
    confidence = vitals.source_confidence

    if confidence >= 0.85:
        level = "HIGH"
        uncertain = False
    elif confidence >= 0.60:
        level = "MEDIUM"
        uncertain = True
    else:
        level = "LOW"
        uncertain = True

    return {
        "confidence": confidence,
        "level": level,
        "is_uncertain": uncertain,
    }


if __name__ == "__main__":
    from datetime import datetime

    test_vitals = VitalSignsReading(
        heart_rate=112.0,
        spo2=91.0,
        blood_pressure_sys=120.0,
        blood_pressure_dia=80.0,
        resp_rate=22.0,
        timestamp=datetime.now(),
        source_confidence=0.90,
    )

    result = assess_confidence(test_vitals)

    print("[Layer 3.3] Confidence assessment")
    print("Confidence:", result["confidence"])
    print("Level:", result["level"])
    print("Uncertain:", result["is_uncertain"])