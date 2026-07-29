"""cosmic-moment — discrete moments of cosmic emergence."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version

try:
    __version__ = _version("cosmic-moment")
except PackageNotFoundError:
    # Not installed, e.g. running from source.
    __version__ = "0.0.0+unknown"

__author__ = "GenesisAeon Team"
