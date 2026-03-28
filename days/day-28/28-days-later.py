from collections import deque

def days_to_infect(city: list) -> int:
    if not isinstance(city, list) or not all(isinstance(row, list) for row in city):
        raise TypeError("La ciudad debe ser una lista de listas.")

    if not city or not city[0]:
        return 0

    rows, cols = len(city), len(city[0])

    valid = {'👤', '🧟', ' '}
    for row in city:
        for cell in row:
            if cell not in valid:
                raise ValueError(f"Valor inválido: {cell}")

    # deque se usa como una cola eficiente (FIFO)
    # Permite agregar al final y sacar del inicio en O(1)
    queue = deque()
    healthy = 0

    for r in range(rows):
        for c in range(cols):
            if city[r][c] == '🧟':
                # Se agregan las posiciones infectadas iniciales a la cola
                queue.append((r, c))
            elif city[r][c] == '👤':
                healthy += 1

    if healthy == 0:
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    days = 0

    # Mientras haya elementos en la cola, seguimos propagando la infección
    while queue:
        size = len(queue)
        infected = False

        # Procesamos todos los elementos actuales de la cola
        # Esto representa un "día" completo en la simulación
        for _ in range(size):
            # popleft() extrae el primer elemento (FIFO)
            # Es eficiente gracias a deque (O(1))
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if city[nr][nc] == '👤':
                        city[nr][nc] = '🧟'
                        healthy -= 1

                        # Nuevos infectados se agregan al final de la cola
                        # Serán procesados en el siguiente "día"
                        queue.append((nr, nc))
                        infected = True

        if infected:
            days += 1

    return days if healthy == 0 else -1