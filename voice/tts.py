from typing import Optional
import pyttsx3
import threading

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

class TextToSpeech:
    

    def __init__(self, config: AudioConfig):
        self.config = config
        self._engine = None

    def _init_engine(self):
        if self._engine is None:
            self._engine = pyttsx3.init()
            self._engine.setProperty("rate", self.config.tts_rate)
            self._engine.setProperty("volume", self.config.tts_volume)

    def list_voices(self):
        """Prints all available TTS voices."""
        self._init_engine()
        voices = self._engine.getProperty("voices")
        for i, v in enumerate(voices):
            print(f"  [{i}] {v.name} | {v.languages} | {v.id}")

    def set_voice(self, voice_index: int):
        """Set voice by index from list_voices()."""
        self._init_engine()
        voices = self._engine.getProperty("voices")
        if 0 <= voice_index < len(voices):
            self._engine.setProperty("voice", voices[voice_index].id)

    def speak(self, text: str):
        """Speaks text aloud (blocking)."""
        self._init_engine()
        print(f"[TTS] Speaking: {text[:80]}{'...' if len(text) > 80 else ''}")
        self._engine.say(text)
        self._engine.runAndWait()

    def speak_async(self, text: str):
        """Speaks in a separate thread (non-blocking)."""
        t = threading.Thread(target=self.speak, args=(text,), daemon=True)
        t.start()
        return t

    def save_to_file(self, text: str, filepath: str):
        """Save TTS output to WAV file."""
        self._init_engine()
        self._engine.save_to_file(text, filepath)
        self._engine.runAndWait()
        print(f"[TTS] Saved to {filepath}")