"""Utils for datetime operations."""

from datetime import timedelta


def format_time_delta(delta: timedelta) -> str:
    """Format a timedelta as minutes and seconds."""
    delta_f = f"{delta.seconds // 60}m {delta.seconds % 60}s"
    return delta_f


FMT_DATETIME = "%Y%m%d_%H%M%S"
