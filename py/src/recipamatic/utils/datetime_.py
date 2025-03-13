"""Utils for datetime operations."""

from datetime import datetime, timedelta


def format_time_delta(delta: timedelta) -> str:
    """Format a timedelta as minutes and seconds."""
    delta_f = f"{delta.seconds // 60}m {delta.seconds % 60}s"
    return delta_f


def generate_timestamp_code() -> str:
    """Generate a formatted timestamp code using the current datetime.

    Returns:
        str: A timestamp string formatted according to FMT_DATETIME

    Note:
        This function may produce duplicate codes if called multiple times within
        the same second.
    """
    timestamp: datetime = datetime.now()
    return timestamp.strftime(FMT_DATETIME)


FMT_DATETIME = "%Y%m%d_%H%M%S"
