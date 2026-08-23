from shared.schema import VitalSignsReading
from reason import analyze_vitals


def interpret_vitals(vitals: VitalSignsReading) -> str:
    result = analyze_vitals(vitals)
    findings = result["findings"]

    abnormal_findings = [
        finding
        for finding in findings
        if finding != "No abnormal vital sign detected."
    ]

    if len(abnormal_findings) >= 2:
        return "Multiple abnormal vital signs detected."

    if len(abnormal_findings) == 1:
        return abnormal_findings[0]

    return "Vital signs are within the configured normal ranges."


if __name__ == "__main__":
    from datetime import datetime

    test_vitals = VitalSignsReading(
        heart_rate=112.0,
        spo2=91.0,
        blood_pressure_sys=120.0,
        blood_pressure_dia=80.0,
        resp_rate=22.0,
        timestamp=datetime.now(),
        source_confidence=0.0,
    )

    interpretation = interpret_vitals(test_vitals)

    print("[Layer 3.2] Overall interpretation")
    print("Interpretation:", interpretation)