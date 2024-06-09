def get_pay_amount():
    result: float = 0
    if is_dead:
        result = dead_amount()
    else:
        if is_seperated:
            result = seperated_amount()
        else:
            result = normal_amount()
    return result
