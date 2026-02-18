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


# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

@dataclass
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


# ─────────────────────────────────────────────
# AUDIO CAPTURE
# ─────────────────────────────────────────────

class AudioCapture:
    """Records audio from microphone with auto-stop on silence."""

    def __init__(self, config: AudioConfig):
        self.config = config

    def _rms(self, block: np.ndarray) -> float:
        return float(np.sqrt(np.mean(block.astype(np.float32) ** 2)) / 32768.0)

    def record(self) -> np.ndarray:
        """
        Records until max_record_seconds OR silence_duration seconds of silence.
        Returns numpy array of audio samples.
        """
        cfg = self.config
        block_size = int(cfg.sample_rate * 0.1)  # 100ms blocks
        max_blocks = int(cfg.max_record_seconds / 0.1)
        silence_blocks = int(cfg.silence_duration / 0.1)

        frames = []
        silent_count = 0
        recording = True
        speech_started = False

        print("[MIC] Listening... (speak now)")

        with sd.InputStream(
            samplerate=cfg.sample_rate,
            channels=cfg.channels,
            dtype=cfg.dtype,
            blocksize=block_size,
        ) as stream:
            for _ in range(max_blocks):
                block, _ = stream.read(block_size)
                frames.append(block.copy())
                rms = self._rms(block)

                if rms > cfg.silence_threshold:
                    speech_started = True
                    silent_count = 0
                elif speech_started:
                    silent_count += 1
                    if silent_count >= silence_blocks:
                        print("[MIC] Silence detected. Stopping.")
                        break

        if not frames:
            return np.array([], dtype=np.int16)

        audio = np.concatenate(frames, axis=0).flatten()
        print(f"[MIC] Captured {len(audio) / cfg.sample_rate:.2f}s of audio")
        return audio

    def record_to_file(self) -> str:
        """Records and saves to a temp WAV file. Returns file path."""
        audio = self.record()
        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        wav_write(tmp.name, self.config.sample_rate, audio)
        return tmp.name

    def play_audio_file(self, filepath: str):
        """Plays back a WAV file (for testing)."""
        rate, data = wav_read(filepath)
        sd.play(data, rate)
        sd.wait()
