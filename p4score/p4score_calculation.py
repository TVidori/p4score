
def calculate_p4score(
        true_positive: int,
        false_negative: int,
        false_positive: int,
        true_negative: int,
) -> float:
    if true_positive == 0 or false_negative == 0:
        return 0.0

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    specificity = true_negative / (true_negative + false_positive)
    npv = true_negative / (true_negative + false_negative)

    return (4 / (
        1 / precision + 1 / recall + 1 / specificity + 1 / npv
    ))

