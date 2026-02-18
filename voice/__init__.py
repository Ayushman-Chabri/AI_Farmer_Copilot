from typing import Optional

class AudioConfig:
    sample_rate: int = 16000          # Whisper expects 16kHz
    channels: int = 1                 # Mono
    dtype: str = "int16"              # 16-bit PCM
    max_record_seconds: int = 10      # Max mic capture duration
    silence_threshold: float = 0.01  # RMS below this = silence
    silence_duration: float = 1.5    # Seconds of silence to auto-stop
    whisper_model: str = "small"      # tiny/base/small (offline)
    language: Optional[str] = None    # None = auto-detect; "hi", "or", "en" etc.
    tts_rate: int = 150               # Words per minute for TTS
    tts_volume: float = 1.0           # 0.0 to 1.0
