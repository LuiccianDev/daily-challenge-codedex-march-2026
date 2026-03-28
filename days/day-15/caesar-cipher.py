def decode_message(message: str, shift: int) -> str:

    #  Validations 
    if not isinstance(message, str):
        raise TypeError("message must be a string")

    if not isinstance(shift, int):
        raise TypeError("shift must be an integer")

    if shift < 0:
        raise ValueError("shift must be >= 0")

    for char in message:
        if not (char.islower() or char == " "):
            raise ValueError(
                "message must contain only lowercase letters and spaces"
            )

    # Decode
    decoded = []

    for char in message:

        if char == " ":
            decoded.append(" ")
            continue

        # convert letter → number (0–25)
        pos = ord(char) - ord('a')

        # shift backwards
        new_pos = (pos - shift) % 26

        # convert number → letter
        new_char = chr(new_pos + ord('a'))

        decoded.append(new_char)

    return "".join(decoded)