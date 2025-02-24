import numpy as np


def convert_predictions_to_confusion_matrix(
        predictions: np.ndarray,
        actual_values: np.ndarray,
) -> tuple[int, int, int, int]:
    true_positive = np.count_nonzero(
        np.logical_and(actual_values, predictions)
    )
    false_negative = np.count_nonzero(
        np.logical_and(actual_values, ~predictions)
    )
    false_positive = np.count_nonzero(
        np.logical_and(~actual_values, predictions)
    )
    true_negative = np.count_nonzero(
        np.logical_and(~actual_values, ~predictions)
    )

    return (
        true_positive,
        false_negative,
        false_positive,
        true_negative,
    )
