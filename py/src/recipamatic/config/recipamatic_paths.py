"""Paths and folders for data files."""

from pathlib import Path

from loguru import logger as lg

import recipamatic


class RecipamaticPaths:
    """Paths and folders for data and resources."""

    def __init__(
        self,
    ) -> None:
        """Load the config for data folders."""
        self.load_config()

    def load_config(self) -> None:
        """Load the config for data folders."""
        self.load_common_config_pre()

    def load_common_config_pre(self) -> None:
        """Pre load the common config."""
        # src folder of the package
        self.src_fol = Path(recipamatic.__file__).parent
        # root folder of the python project
        self.root_py_fol = self.src_fol.parents[1]
        # root folder of the whole project
        self.root_fol = self.root_py_fol.parent
        # cache
        self.cache_fol = self.root_fol / "cache"
        # data
        self.data_fol = self.root_fol / "data"
        # static
        self.static_fol = self.root_fol / "static"

    def __str__(self) -> str:
        s = f"RecipamaticPaths:\n"
        s += f"   src_fol: {self.src_fol}\n"
        s += f"  root_fol: {self.root_fol}\n"
        s += f" cache_fol: {self.cache_fol}\n"
        s += f"  data_fol: {self.data_fol}\n"
        s += f"static_fol: {self.static_fol}\n"
        return s
