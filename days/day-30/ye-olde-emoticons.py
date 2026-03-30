def emoticons_mood(message):
  
    # Validación de entrada
    if not isinstance(message, str):
        raise TypeError("El parámetro 'message' debe ser una cadena de texto.")
    if not message:
        return 0  # Mensaje vacío → sin impacto

    # Constantes de moticonos felices
    happy_emoticons = {":)", ":p", "XD", ":3", "<3", r"\m/"}

    # Constantes de emoticonos tristes
    sad_emoticons = {":(", ":'(", "t(-.-t)"}

    score = 0
    # contar ocurrencias de cada emoticono
    for emoticon in happy_emoticons:
        score += message.count(emoticon)

    for emoticon in sad_emoticons:
        score -= message.count(emoticon)

    return score