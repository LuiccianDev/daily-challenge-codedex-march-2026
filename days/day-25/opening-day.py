def streak_counter(games: list) -> int:
    #  Validations 
    if not isinstance(games, list):
        raise TypeError("games must be a list")

    valid_values = {"W", "L", "R"}

    for g in games:
        if not isinstance(g, str):
            raise TypeError("Each game must be a string")

        if g not in valid_values:
            raise ValueError(f"Invalid value: {g}")
    # main codigo principal 
    max_streak = 0
    current_streak = 0

    for result in games:
        if result == "W":
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        elif result == "L":
            current_streak = 0
        elif result == "R":
            continue

    return max_streak