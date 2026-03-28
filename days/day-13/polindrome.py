def check_palindrome(sequence: str) -> bool:

    # Validate input
    if not isinstance(sequence, str):
        return False

    # Normalize string (remove spaces and lowercase)
    clean = sequence.replace(" ", "").lower()

    # Check palindrome
    return clean == clean[::-1]