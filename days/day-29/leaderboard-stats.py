def average_time(total, completed):

    # Validations
    if not isinstance(total, str):
        raise TypeError("total must be a string in format 'H:MM:SS'")
    if not isinstance(completed, int):
        raise TypeError("completed must be an integer")
    if completed <= 0:
        raise ValueError("completed must be greater than 0")

    # try and except
    try:
        # Use map
        hours, minutes, seconds = map(int, total.split(":"))
    except ValueError:
        raise ValueError("Invalid time format. Expected 'H:MM:SS'")

    if minutes < 0 or minutes >= 60 or seconds < 0 or seconds >= 60:
        raise ValueError("Minutes and seconds must be between 0 and 59")

    total_seconds = hours * 3600 + minutes * 60 + seconds
    average = total_seconds / completed

    return round(average)  