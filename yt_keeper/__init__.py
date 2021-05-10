from pathlib import Path

RELATIVE_ROOT = Path(__file__).parent.parent

from . import config  # noqa: 402
CONFIG = config.load()
