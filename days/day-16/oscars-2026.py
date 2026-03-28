def oscar_pool(predictions):
    # Lista oficial de ganadores (orden fijo)
    winners = [
        "One Battle After Another",
        "Michael B. Jordan",
        "Jessie Buckley",
        "Paul Thomas Anderson"
    ]

    # Validación básica
    if not isinstance(predictions, list) or len(predictions) == 0:
        raise ValueError("predictions debe ser una lista no vacía")

    best_name = None
    best_score = -1
    tie = False

    for friend in predictions:
        # Validar formato de cada predicción
        if not isinstance(friend, list) or len(friend) != 5:
            raise ValueError(
                "Cada predicción debe tener 5 elementos: nombre + 4 predicciones"
            )

        name = friend[0]
        guesses = friend[1:]

        correct = 0

        # Contar aciertos
        for i in range(len(winners)):
            if guesses[i] == winners[i]:
                correct += 1

        # Calcular accuracy (no necesario para comparar, pero claro)
        accuracy = correct / len(winners)

        # Comparar con el mejor actual
        if correct > best_score:
            best_score = correct
            best_name = name
            tie = False
        elif correct == best_score:
            tie = True

    return "Tie" if tie else best_name