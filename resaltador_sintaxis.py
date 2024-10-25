def resaltar_sintaxis(regex):
    resaltado = ""
    # Definir colores para diferentes patrones
    for char in regex:
        if char == '\\d':
            resaltado += f"{char} (azul) "  # Aquí deberías poner el texto que representa azul
        elif char == '\\w':
            resaltado += f"{char} (verde) "  # Aquí deberías poner el texto que representa verde
        elif char == '\\s':
            resaltado += f"{char} (rojo) "  # Aquí deberías poner el texto que representa rojo
        else:
            resaltado += char + " "  # Agregar carácter normal sin resaltado
    return resaltado
