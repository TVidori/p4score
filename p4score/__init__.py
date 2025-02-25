from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("p4score")
except PackageNotFoundError:
    __version__ = "unknown"

from p4score.p4score_calculation import (
    calculate_p4score,
    calculate_p4score_from_predictions,
)
