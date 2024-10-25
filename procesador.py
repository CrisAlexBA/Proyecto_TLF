import re
from tkinter import messagebox

def validar_cadenas(regex, cadenas):
    """Valida cada cadena contra la expresión regular."""
    try:
        resultado = []
        for cadena in cadenas:
            if re.fullmatch(regex, cadena):
                resultado.append(f"'{cadena}' es ACEPTADA")
            else:
                resultado.append(f"'{cadena}' es RECHAZADA")
        return "\n".join(resultado)
    except re.error:
        messagebox.showerror("Error", "Expresión regular no válida")
        return ""

def explicar_regex(regex):
    """Explica la expresión regular en términos sencillos."""
    explicacion = []
    if '(' in regex:
        explicacion.append("Usas paréntesis para agrupar partes de la expresión.")
    if '.' in regex:
        explicacion.append("El punto (.) representa cualquier carácter.")
    if '*' in regex:
        explicacion.append("El asterisco (*) indica que el carácter anterior puede repetirse cero o más veces.")
    messagebox.showinfo("Explicación de la Expresión", "\n".join(explicacion))
