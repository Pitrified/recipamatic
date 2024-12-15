"""Test that the environment variables are available."""

import os

import pytest


def test_env_vars() -> None:
    """The environment var RECIPAMATIC_SAMPLE_ENV_VAR is available."""
    assert "RECIPAMATIC_SAMPLE_ENV_VAR" in os.environ
    assert os.environ["RECIPAMATIC_SAMPLE_ENV_VAR"] == "sample"
