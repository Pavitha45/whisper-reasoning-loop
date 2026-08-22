import re


def parse_query(text):
    text = text.lower().strip()

    if "heart rate" in text or "hr" in text:
        return {
            "intent": "CURRENT_VITAL",
            "vital": "heart_rate",
            "query": text,
        }

    if "spo2" in text or "oxygen" in text or "saturation" in text:
        return {
            "intent": "CURRENT_VITAL",
            "vital": "spo2",
            "query": text,
        }

    if "blood pressure" in text or "bp" in text:
        return {
            "intent": "CURRENT_VITAL",
            "vital": "blood_pressure",
            "query": text,
        }

    if "respiratory rate" in text or "resp rate" in text:
        return {
            "intent": "CURRENT_VITAL",
            "vital": "respiratory_rate",
            "query": text,
        }

    return {
        "intent": "UNKNOWN",
        "vital": None,
        "query": text,
    }


if __name__ == "__main__":
    test_query = "Which is the current heart rate?"
    result = parse_query(test_query)

    print("[Layer 2.3] Query parsing successful.")
    print("Input :", test_query)
    print("Output:", result)
