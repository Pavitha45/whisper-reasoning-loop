from shared.schema import VitalSignsReading

from parse_query import parse_query
from answer_query import answer_query

import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "layer3_reasoning"
    )
)

from build_answer import build_reasoning_answer


def process_query(text: str, vitals: VitalSignsReading) -> str:
    parsed = parse_query(text)

    if parsed["intent"] == "UNKNOWN":
        return "I could not identify the requested vital sign."

    direct_answer = answer_query(text, vitals)
    reasoning_answer = build_reasoning_answer(vitals)

    return (
        f"{direct_answer}\n"
        f"Reasoning: {reasoning_answer.answer_text}\n"
        f"Confidence: {reasoning_answer.confidence:.2f}\n"
        f"Uncertain: {reasoning_answer.is_uncertain}"
    )


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

    test_query = "Which is the current heart rate?"

    print("[Layer 2.6] Ear → Reasoning integration")
    print("Query:", test_query)
    print()
    print(process_query(test_query, test_vitals))
