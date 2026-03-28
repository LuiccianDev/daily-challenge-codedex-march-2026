def calculate_sleep_debt(planned, actual):

    # Validate input lengths
    if len(planned) != len(actual):
        raise ValueError("Planned and actual sleep lists must have the same length.")

    total_debt = 0
    current_streak = 0
    longest_streak = 0

    for planned_hours, actual_hours in zip(planned, actual):
        # Daily sleep debt
        daily_debt = max(0, planned_hours - actual_hours)

        # Accumulate total debt
        total_debt += daily_debt

        # Track streaks
        if daily_debt > 0:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0

    # Add the Daylight Savings lost hour
    total_debt += 1

    return total_debt, longest_streak