def pick_voucher(vouchers, delays, max_wait):
    #  Validations 
    if not isinstance(vouchers, list) or not isinstance(delays, list):
        raise TypeError("vouchers and delays must be lists")

    if len(vouchers) != len(delays):
        raise ValueError("vouchers and delays must have the same length")

    if not isinstance(max_wait, (int, float)):
        raise TypeError("max_wait must be a number")

    best_index = -1
    best_ratio = -1
    for i in range(len(vouchers)):

        amount = vouchers[i]
        delay = delays[i]

        # Skip invalid values
        if delay <= 0:
            continue

        if delay > max_wait:
            continue

        ratio = amount / delay

        if ratio > best_ratio:
            best_ratio = ratio
            best_index = i

    return best_index