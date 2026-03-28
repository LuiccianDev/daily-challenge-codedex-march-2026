def cuddly_kittens(kittens: list[int], limit: int) -> int:
    #  Validations
    # Check type of kittens
    if not isinstance(kittens, list):
        raise TypeError("kittens must be a list")
    # Check type of limit
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    # Check empty list
    if len(kittens) == 0:
        return 0
    # Check negative limit
    if limit < 0:
        raise ValueError("limit must be >= 0")
    # Check all elements are integers
    for k in kittens:
        if not isinstance(k, int):
            raise TypeError("all energy levels must be integers")

    left = 0
    max_len = 0

    for right in range(len(kittens)):
        # Shrink window while condition is invalid
        while max(kittens[left:right+1]) - min(kittens[left:right+1]) > limit:
            left += 1
        # Update max length
        current_len = right - left + 1
        max_len = max(max_len, current_len)

    return max_len