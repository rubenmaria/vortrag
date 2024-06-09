def bafoeg_amount() -> float:
    if age < 45:
        return 0
    if not is_studying:
        return 0
    if is_rich:
        return 0
    return compute_bafoeg_amount()
