import os

def WriteToFile(filename: str, content: str):
    # Obtener el directorio de la ruta
    directory = os.path.dirname(filename)

    # Crear el directorio si no existe
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Escribir en el archivo
    with open(filename, 'w') as _file:
        _file.write(content)

    return f'File "{filename}" created!'
