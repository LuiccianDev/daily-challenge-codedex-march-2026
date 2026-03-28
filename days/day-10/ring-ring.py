def find_unique_words(transcript):
    # validar que sea texto
    if not isinstance(transcript, str):
        return 0

    # convertir a minusculas
    text = transcript.lower()

    # quitar puntuacion
    cleaned = ""
    for c in text:
        if c.isalnum() or c == " ":
            cleaned += c

    # separar palabras
    words = cleaned.split()

    # usar set para palabras unicas
    unique_words = set(words)

    # devolver cantidad
    return len(unique_words)