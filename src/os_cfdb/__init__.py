import importlib.metadata

_DISTRIBUTION_METADATA = importlib.metadata.metadata("os-cfdb")

__version__ = _DISTRIBUTION_METADATA["Version"]
