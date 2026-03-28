def leaky_pipe(volume: float,leak: float,hours: int,threshold: float) :

    # validation
    if volume < 0:
        raise ValueError("volume must be >= 0")
    if not (0 <= leak <= 100):
        raise ValueError("leak must be between 0 and 100")
    if hours < 0:
        raise ValueError("hours must be >= 0")
    if threshold < 0:
        raise ValueError("threshold must be >= 0")

    current_volume = float(volume)

    for _ in range(hours):
        current_volume *= (1 - leak / 100)
        # check failure
        if current_volume < threshold:
            return -1
    # result
    return round(current_volume, 2)  