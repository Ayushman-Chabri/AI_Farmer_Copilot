import os
import time
import tempfile
import threading
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write as wav_write
from scipy.io.wavfile import read as wav_read
import whisper
import pyttsx3
from dataclasses import dataclass
from typing import Optional

@dataclass
class AudioConfig:
    """Configuration for speech-to-text processing."""
    whisper_model: str = "base"
    language: Optional[str] = None
    sample_rate: int = 16000

class SpeechToText:
    """
    Offline STT using OpenAI Whisper.
    Supports Hindi, Odia, Bengali, English, etc.
    """

    def __init__(self, config: AudioConfig):
        self.config = config
        self._model = None
        self._lock = threading.Lock()

    def _load_model(self):
        if self._model is None:
            print(f"[STT] Loading Whisper '{self.config.whisper_model}' model...")
            self._model = whisper.load_model(self.config.whisper_model)
            print("[STT] Model loaded.")

    def transcribe(self, audio_input) -> dict:
        """
        Transcribe from:
          - numpy array (int16, 16kHz)
          - file path (str)

        Returns: {
            "text": str,
            "language": str,
            "confidence": float (avg log-prob proxy),
            "success": bool
        }
        """
        with self._lock:
            self._load_model()

        try:
            # If numpy array, save to temp file
            if isinstance(audio_input, np.ndarray):
                tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
                wav_write(tmp.name, self.config.sample_rate, audio_input)
                filepath = tmp.name
                cleanup = True
            else:
                filepath = audio_input
                cleanup = False

            options = {}
            if self.config.language:
                options["language"] = self.config.language

            result = self._model.transcribe(filepath, **options)

            text = result.get("text", "").strip()
            language = result.get("language", "unknown")

            # Confidence: average of segment log-probs (if available)
            segments = result.get("segments", [])
            if segments:
                avg_logprob = np.mean([s.get("avg_logprob", -1.0) for s in segments])
                confidence = float(np.exp(avg_logprob))  # convert to 0-1 scale
            else:
                confidence = 0.0

            if cleanup:
                os.unlink(filepath)

            return {
                "text": text,
                "language": language,
                "confidence": confidence,
                "success": bool(text),
            }

        except Exception as e:
            print(f"[STT] Error: {e}")
            return {"text": "", "language": "unknown", "confidence": 0.0, "success": False}

    def validate(self, result: dict, min_confidence: float = 0.3) -> bool:
        """Returns True if transcription is likely valid."""
        return result["success"] and result["confidence"] >= min_confidence