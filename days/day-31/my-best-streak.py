def longest_streak(progress):
    # Validación de tipo
    if not isinstance(progress, list):
        raise TypeError("El parámetro debe ser una lista.")

    # Validación de contenido
    valid_values = {'✅', '❌'}
    for i, value in enumerate(progress):
        if not isinstance(value, str):
            raise TypeError(f"El elemento en la posición {i} no es un string.")
        if value not in valid_values:
            raise ValueError(f"Valor inválido en la posición {i}: {value}")

    max_streak = 0
    current_streak = 0

    # Lógica principal
    for day in progress:
        if day == '✅':
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0

    return max_streak