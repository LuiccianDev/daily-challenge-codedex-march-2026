def infinite_monkey(target: str, attempt: str) -> dict:
    # Validaciones
    if not isinstance(target, str) or not isinstance(attempt, str):
        raise TypeError("Ambos parámetros deben ser strings.")
    if len(target) == 0:
        raise ValueError("El target no puede estar vacío.")
    if len(attempt) < len(target):
        raise ValueError("El attempt debe ser más largo o igual al target.")

    target_length = len(target)
    best_index = 0
    best_matches = 0

    # Sliding window
    for i in range(len(attempt) - target_length + 1):
        matches = 0
        for j in range(target_length):
            if attempt[i + j] == target[j]:
                matches += 1
        # Mantener el primero en caso de empate
        if matches > best_matches:
            best_matches = matches
            best_index = i

    # Similitud
    similarity_raw = (best_matches / target_length) * 100
    similarity = round(similarity_raw, 2)

    # Intentos
    if similarity_raw == 0:
        attempts = None
    else:
        attempts = round((100 / similarity_raw) ** target_length)

    return {
        "best_index": best_index,
        "similarity": similarity,
        "attempts": attempts
    }

