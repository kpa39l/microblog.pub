import logging
from datetime import datetime
from datetime import timezone

from dateutil import parser

logger = logging.getLogger(__name__)


def strtobool(s: str) -> bool:
    if s in ["y", "yes", "true", "on", "1"]:
        return True
    if s in ["n", "no", "false", "off", "0"]:
        return False

    raise ValueError(f"cannot convert {s} to bool")


def parse_datetime(s :str) -> datetime:
    # Parses the datetime with dateutil
    dt = parser.parse(s)

    # If no TZ is set, assumes it's UTC
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=timezone.utc)

    return dt
