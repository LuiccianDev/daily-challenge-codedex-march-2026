def wordle_guess(secret, guess):
    try:
        # Check that both inputs are strings
        if not isinstance(secret, str) or not isinstance(guess, str):
            raise TypeError("Both inputs must be strings.")
        
        # Normalize to uppercase 
        secret = secret.strip().upper()
        guess = guess.strip().upper()

        # Validate same length
        if len(secret) != len(guess):
            raise ValueError("Both strings must have the same length.")
        
        return sum(s == g for s, g in zip(secret, guess))

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None

