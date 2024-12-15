"""Test the recipamatic paths."""

import pytest

from recipamatic.config.recipamatic_config import get_recipamatic_paths


def test_recipamatic_paths() -> None:
    """Test the recipamatic paths."""
    recipamatic_paths = get_recipamatic_paths()
    assert recipamatic_paths.src_fol.name == "recipamatic"
    assert recipamatic_paths.root_py_fol.name == "py"
    assert recipamatic_paths.root_fol.name == "recipamatic"
    assert recipamatic_paths.data_fol.name == "data"
