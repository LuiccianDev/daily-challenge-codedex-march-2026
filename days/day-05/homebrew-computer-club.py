def dompier_music(switches):
    # Dictionary that maps frequencies (in Hz) to their corresponding music notes
    frequency_to_note = {
        261: "C4",
        294: "D4",
        329: "E4",
        349: "F4",
        392: "G4",
        440: "A4",
        494: "B4",
        523: "C5",
        0: "REST"
    }
    # List to store the resulting notes
    result = []
    # Iterate through each binary string in the switches list
    for binary_value in switches:
        # Convert the binary string into a decimal integer
        decimal_value = int(binary_value, 2)
        # Look up the corresponding note using the dictionary
        note = frequency_to_note.get(decimal_value)
        # Add the note to the result list
        result.append(note)
    # Return the final list of music notes
    return result