from datetime import datetime


def iso_to_datetime(iso_timestamp: str) -> datetime:
    """Convert an ISO 8601 string with Z timezone to a datetime object."""
    return datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))
