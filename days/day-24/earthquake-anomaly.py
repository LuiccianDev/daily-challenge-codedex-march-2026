def earthquake_anomaly(readings: list[float]) -> list[int]:

    # Validations
    if not isinstance(readings, list):
        raise TypeError("readings must be a list")
    if len(readings) == 0:
        return []
    for r in readings:
        if not isinstance(r, (int, float)):
            raise TypeError("all readings must be numbers")
        if r < 0:
            raise ValueError("magnitude cannot be negative")

    # Calculate median
    sorted_readings = sorted(readings)
    n = len(sorted_readings)

    if n % 2 == 1:
        median = sorted_readings[n // 2]
    else:
        mid1 = sorted_readings[n // 2 - 1]
        mid2 = sorted_readings[n // 2]
        median = (mid1 + mid2) / 2

    # Threshold
    threshold = 1.5 * median
    # Find anomalies
    anomalies = []

    for i, value in enumerate(readings):
        if value > threshold:
            anomalies.append(i)

    return anomalies