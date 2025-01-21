"""Wrapper for whisper model."""

from pathlib import Path

from loguru import logger as lg
import whisper
from whisper import Whisper

from recipamatic.api.models import AudioFile
from recipamatic.config.recipamatic_config import get_recipamatic_paths


class Whisperer:
    """Wrapper for whisper model."""

    def __init__(
        self,
        model_name: str = "medium",
    ) -> None:
        """Initialize Whisperer object."""
        # set model name
        self.model_name = model_name

        # load available models and check if model_name is available
        self.load_available_models()
        if model_name not in self.available_models:
            lg.error(f"Model {model_name} not available.")
            lg.info(f"Available models: {self.available_models}")
            raise ValueError(f"Model {model_name} not available.")

        # load model
        self.model = whisper.load_model(model_name)

    def load_available_models(self) -> None:
        """Load available models."""
        self.available_models = whisper.available_models()

    def extract_text(
        self,
        audio_fp: Path,
        **kwargs,
    ) -> str:
        """Extract text from audio file."""
        result = self.model.transcribe(str(audio_fp), **kwargs)
        # Returns A dictionary containing the resulting text ("text") and
        # segment-level details ("segments"), and the spoken language ("language"),
        # which is detected when decode_options["language"] is None.
        text = result["text"]
        if not isinstance(text, str):
            lg.warning(f"Got {text} of type {type(text)}")
            raise ValueError(f"Expected text to be a string, but got {type(text)}")
        return text

    def extract_text_from_audio_file(
        self,
        audio_file: AudioFile,
        **kwargs,
    ) -> str:
        """Extract text from audio file."""
        audio_fol = get_recipamatic_paths().notes_fol
        audio_fp = audio_fol / audio_file.filename
        # save the bytes to a file
        with open(audio_fp, "wb") as f:
            f.write(audio_file.content)
        return self.extract_text(audio_fp, **kwargs)
