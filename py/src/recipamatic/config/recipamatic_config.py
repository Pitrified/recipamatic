"""Recipamatic project configuration."""

from loguru import logger as lg

from recipamatic.config.recipamatic_paths import RecipamaticPaths
from recipamatic.config.singleton import Singleton


class RecipamaticConfig(metaclass=Singleton):
    """Recipamatic project configuration."""

    def __init__(self) -> None:
        lg.info(f"Loading Recipamatic config")
        self.paths = RecipamaticPaths()

    def __str__(self) -> str:
        s = "RecipamaticConfig:"
        s += f"\n{self.paths}"
        return s

    def __repr__(self) -> str:
        return str(self)


def get_recipamatic_config() -> RecipamaticConfig:
    """Get the recipamatic config."""
    return RecipamaticConfig()


def get_recipamatic_paths() -> RecipamaticPaths:
    """Get the recipamatic paths."""
    return get_recipamatic_config().paths
