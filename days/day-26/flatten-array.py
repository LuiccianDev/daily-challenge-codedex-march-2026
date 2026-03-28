from typing import Any

def flatten(data: list) -> list:

    # Validación de entrada
    if not isinstance(data, list):
        raise TypeError("El parámetro debe ser una lista.")

    result = []

    def _flatten(element: Any) -> None:
        """
        Función auxiliar recursiva para aplanar la lista.
        """
        if isinstance(element, list):
            for item in element:
                _flatten(item)
        else:
            result.append(element)

    _flatten(data)

    return result