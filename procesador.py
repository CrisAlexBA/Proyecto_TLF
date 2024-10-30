import re
from tkinter import messagebox

def validar_cadenas(regex, cadenas):
    """Valida cada cadena contra la expresión regular"""
    try:
        resultado = []
        patron = re.compile(regex)  # Compilar la expresión regular
        for cadena in cadenas:
            if patron.fullmatch(cadena):
                resultado.append(f"'{cadena}' es ACEPTADA")
            else:
                resultado.append(f"'{cadena}' es RECHAZADA")
        return "\n".join(resultado)
    except re.error:
        messagebox.showerror("Error", "Expresión regular no válida")
        return ""

def explicar_regex(regex):
    """Explica la expresión regular en términos sencillos"""
    explicacion = []
    if '(' in regex:
        explicacion.append("Usas paréntesis para agrupar partes de la expresión.")
    if '.' in regex:
        explicacion.append("El punto (.) representa cualquier carácter.")
    if '*' in regex:
        explicacion.append("El asterisco (*) indica que el carácter anterior puede repetirse cero o más veces.")
    if '|' in regex:
        explicacion.append("La barra vertical (|) indica una opción entre alternativas.")
    if '+' in regex:
        explicacion.append("El signo más (+) indica que el carácter anterior debe aparecer una o más veces.")
    return "\n".join(explicacion)
