from datetime import datetime

from shared.schema import VitalSignsReading, ReasoningAnswer
from reason import analyze_vitals
from confidence import assess_confidence


def build_reasoning_answer(vitals: VitalSignsReading) -> ReasoningAnswer:
    analysis = analyze_vitals(vitals)
    confidence = assess_confidence(vitals)

    findings = analysis["findings"]

    if len(findings) == 1 and findings[0] == "No abnormal vital sign detected.":
        answer_text = "No abnormal vital sign detected."
    elif len(findings) >= 2:
        answer_text = "Multiple abnormal vital signs detected: " + " ".join(findings)
    else:
        answer_text = findings[0]

    return ReasoningAnswer(
        answer_text=answer_text,
        confidence=confidence["confidence"],
        is_uncertain=confidence["is_uncertain"],
        supporting_data=analysis["vital_signs"],
        timestamp=datetime.now(),
    )


if __name__ == "__main__":
    test_vitals = VitalSignsReading(
        heart_rate=112.0,
        spo2=91.0,
        blood_pressure_sys=120.0,
        blood_pressure_dia=80.0,
        resp_rate=22.0,
        timestamp=datetime.now(),
        source_confidence=0.90,
    )

    result = build_reasoning_answer(test_vitals)

    print("[Layer 3.4] Structured reasoning answer")
    print("Answer:", result.answer_text)
    print("Confidence:", result.confidence)
    print("Uncertain:", result.is_uncertain)
    print("Supporting data:", result.supporting_data)