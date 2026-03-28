def calculate_score(elements):
    
    # Verificación básica del input
    if not isinstance(elements, list):
        raise ValueError("Elements must be a list")

    total_score = 0

    for element in elements:
        
        # Verificar estructura del elemento
        if not isinstance(element, tuple) or len(element) != 3:
            raise ValueError("Each element must be a tuple: (name, base_value, goe_scores)")
        
        name, base_value, goe_scores = element
        
        # Verificar base value
        if not isinstance(base_value, (int, float)):
            raise ValueError(f"Base value for {name} must be numeric")
        
        # Verificar lista de GOE
        if not isinstance(goe_scores, list) or len(goe_scores) != 9:
            raise ValueError(f"{name} must have exactly 9 GOE scores")
        
        # Verificar rango de GOE
        for score in goe_scores:
            if not isinstance(score, (int, float)) or score < -5 or score > 5:
                raise ValueError(f"Invalid GOE score in {name}")

        # Eliminar el mayor y el menor
        sorted_goe = sorted(goe_scores)
        trimmed_goe = sorted_goe[1:-1]

        # Promedio de los 7 restantes
        avg_goe = sum(trimmed_goe) / len(trimmed_goe)

        # Calcular puntaje del elemento
        element_score = base_value + (avg_goe * 0.1 * base_value)

        total_score += element_score

    # Redondear a 1 decimal
    return round(total_score, 1)