from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional


@dataclass
class VitalSignsReading:
    heart_rate: Optional[float]
    spo2: Optional[float]
    blood_pressure_sys: Optional[float]
    blood_pressure_dia: Optional[float]
    resp_rate: Optional[float]
    timestamp: datetime
    source_confidence: float


@dataclass
class SpeechQuery:
    raw_text: str
    intent: str
    speaker_audio_path: Optional[str]
    timestamp: datetime


@dataclass
class VerifiedRequest:
    speech_query: SpeechQuery
    speaker_id: Optional[str]
    role: Optional[str]
    access_granted: bool
    reason_if_denied: Optional[str]


@dataclass
class ReasoningAnswer:
    answer_text: str
    confidence: float
    is_uncertain: bool
    supporting_data: dict[str, Any]
    timestamp: datetime