from datetime import datetime

from shared.schema import VitalSignsReading
from parse_query import parse_query
from answer_query import answer_query


def process_query(text: str, vitals: VitalSignsReading) -> str:
    parsed = parse_query(text)

    if parsed["intent"] == "UNKNOWN":
        return "I could not identify the requested vital sign."

    return answer_query(text, vitals)


if __name__ == "__main__":
    test_vitals = VitalSignsReading(
        heart_rate=112.0,
        spo2=91.0,
        blood_pressure_sys=120.0,
        blood_pressure_dia=80.0,
        resp_rate=22.0,
        timestamp=datetime.now(),
        source_confidence=0.0,
    )

    test_query = "Which is the current heart rate?"

    print("[Layer 2.5] Processing query...")
    result = process_query(test_query, test_vitals)

    print("Query :", test_query)
    print("Answer:", result)