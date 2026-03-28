def find_missing_colors(grid):
    # Lista oficial de colores en orden
    all_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
    
    # Convertimos la grilla en un conjunto de colores encontrados
    found_colors = set()
    for row in grid:
        for color in row:
            found_colors.add(color)
    
    # Encontrar los que faltan manteniendo el orden original
    missing = [color for color in all_colors if color not in found_colors]
    
    return missing