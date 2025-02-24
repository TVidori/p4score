import numpy as np

from p4score import conversion_functions


def calculate_p4score(
        true_positive: int,
        false_negative: int,
        false_positive: int,
        true_negative: int,
) -> float:
    if true_positive == 0 or true_negative == 0:
        return 0.0

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    specificity = true_negative / (true_negative + false_positive)
    npv = true_negative / (true_negative + false_negative)

    return (4 / (
        1 / precision + 1 / recall + 1 / specificity + 1 / npv
    ))


def calculate_p4score_from_predictions(
        predictions: np.ndarray,
        actual_values: np.ndarray,
) -> float:
    (
        true_positive,
        false_negative,
        false_positive,
        true_negative,
    ) = conversion_functions.convert_predictions_to_confusion_matrix(
        predictions=predictions,
        actual_values=actual_values,
    )

    return calculate_p4score(
        true_positive=true_positive,
        false_negative=false_negative,
        false_positive=false_positive,
        true_negative=true_negative,
    )
