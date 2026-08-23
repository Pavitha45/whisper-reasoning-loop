from shared.schema import VitalSignsReading


def answer_query(query: str, vitals: VitalSignsReading) -> str:
    query = query.lower()

    if "heart rate" in query or "hr" in query:
        return f"Current heart rate: {vitals.heart_rate} beats per minute."

    if "spo2" in query or "oxygen" in query or "saturation" in query:
        return f"Current SpO2: {vitals.spo2} percent."

    if "blood pressure" in query or "bp" in query:
        return (
            f"Current blood pressure: "
            f"{vitals.blood_pressure_sys}/{vitals.blood_pressure_dia} mmHg."
        )

    if "respiratory rate" in query or "resp rate" in query:
        return f"Current respiratory rate: {vitals.resp_rate} breaths per minute."

    return "I could not identify the requested vital sign."


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

    query = "Which is the current heart rate?"

    answer = answer_query(query, test_vitals)

    print("[Layer 2.4] Query-to-vital integration successful.")
    print("Query :", query)
    print("Answer:", answer)