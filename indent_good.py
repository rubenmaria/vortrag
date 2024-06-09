def get_pay_amount():
    if is_dead:
        return dead_amount()
    if is_seperated:
        return seperated_amount()
    return normal_amount()
