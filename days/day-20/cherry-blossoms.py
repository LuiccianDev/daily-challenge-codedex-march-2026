def cherry_blossoms(temps: list) -> int:
    #  Validations 
    if not isinstance(temps, list):
        raise TypeError("temps must be a list")

    if len(temps) < 5:
        return -1

    for value in temps:
        if not isinstance(value, (int, float)):
            raise ValueError("All temperatures must be numbers")

    # Config 
    WINDOW_SIZE = 5
    THRESHOLD = 15

    # Rolling average 
    for i in range(WINDOW_SIZE - 1, len(temps)):
        window = temps[i - WINDOW_SIZE + 1 : i + 1]
        average = sum(window) / WINDOW_SIZE
        if average > THRESHOLD:
            return i + 1   # 1-indexed

    return -1