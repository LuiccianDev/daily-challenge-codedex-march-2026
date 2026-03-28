def lucky_river(river, hours):
    # Validaciones
    if not isinstance(river, list):
        raise TypeError("river debe ser una lista")

    if not isinstance(hours, int):
        raise TypeError("hours debe ser un entero")

    if hours < 0:
        raise ValueError("hours debe ser >= 0")

    n = len(river)

    # Si la lista está vacía, retornar igual
    if n == 0:
        return river

    # Copia para no modificar la original
    result = river.copy()

    for _ in range(hours):
        new_state = result.copy()

        for i in range(n):
            if result[i] == "☘️":
                if i + 1 < n:
                    new_state[i + 1] = "☘️"

        result = new_state

    return result