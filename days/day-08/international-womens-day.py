def analyze(percentages):
    # Validation 
    if not percentages or len(percentages) < 3:
        raise ValueError("At least 3 years of data required")

    n = len(percentages)

    # Net Change Per Year 
    first = percentages[0]
    last = percentages[-1]

    net_change_per_year = round((last - first) / (n - 1),4)

    #Trend (compare averages of first 3 vs last 3) 
    first_avg = sum(percentages[:3]) / 3
    last_avg = sum(percentages[-3:]) / 3

    if last_avg > first_avg:
        trend = "improving"
    elif last_avg == first_avg:
        trend = "stagnating"
    else:
        trend = "declining"

    #Dips (count decreases) 
    dips = 0
    for i in range(1, n):
        if percentages[i] < percentages[i - 1]:
            dips += 1

    return net_change_per_year, trend, dips