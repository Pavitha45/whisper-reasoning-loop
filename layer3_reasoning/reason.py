from shared.schema import VitalSignsReading


def analyze_vitals(vitals: VitalSignsReading) -> dict:
    findings = []

    if vitals.heart_rate is not None:
        if vitals.heart_rate > 100:
            findings.append("Heart rate is elevated.")
        elif vitals.heart_rate < 60:
            findings.append("Heart rate is low.")

    if vitals.spo2 is not None:
        if vitals.spo2 < 92:
            findings.append("SpO2 is low.")

    if vitals.resp_rate is not None:
        if vitals.resp_rate > 20:
            findings.append("Respiratory rate is elevated.")

    if not findings:
        findings.append("No abnormal vital sign detected.")

    return {
        "findings": findings,
        "vital_signs": {
            "heart_rate": vitals.heart_rate,
            "spo2": vitals.spo2,
            "blood_pressure": (
                vitals.blood_pressure_sys,
                vitals.blood_pressure_dia,
            ),
            "respiratory_rate": vitals.resp_rate,
        },
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
        source_confidence=0.0,
    )

    result = analyze_vitals(test_vitals)

    print("[Layer 3.1] Vital reasoning test")
    print("Findings:")

    for finding in result["findings"]:
        print("-", finding)