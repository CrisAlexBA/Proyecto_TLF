import tkinter as tk
import re
from procesador import validar_cadenas, explicar_regex
from resaltador_sintaxis import resaltar_sintaxis

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Validador de Expresiones Regulares")

    regex_label = tk.Label(ventana, text="Ingrese expresión regular:")
    regex_label.pack()
    regex_entry = tk.Entry(ventana, width=50)
    regex_entry.pack()
    regex_entry.insert(0, "^[a-zA-Z0-9\\s]*$")  # Inserta la expresión regular por defecto

    cadena_label = tk.Label(ventana, text="Ingrese cadenas (separadas por comas):")
    cadena_label.pack()
    cadena_entry = tk.Entry(ventana, width=50)
    cadena_entry.pack()

    resultado_label = tk.Label(ventana, text="Resultados:")
    resultado_label.pack()
    resultado_text = tk.Text(ventana, height=10, width=50)
    resultado_text.pack()

    syntax_label = tk.Label(ventana, text="Resaltado de Sintaxis:")
    syntax_label.pack()
    highlighted_label = tk.Label(ventana, text="", fg="black", font=("Arial", 10))
    highlighted_label.pack()

    explanation_label = tk.Label(ventana, text="Explicación de la expresión:")
    explanation_label.pack()
    explanation_display = tk.Label(ventana, text="", fg="black", font=("Arial", 10))
    explanation_display.pack()

    validar_button = tk.Button(ventana, text="Validar", command=lambda: validar(regex_entry.get(), cadena_entry.get(), resultado_text))
    validar_button.pack()

    resaltar_button = tk.Button(ventana, text="Resaltar Sintaxis", command=lambda: resaltar(regex_entry.get(), highlighted_label))
    resaltar_button.pack()

    explicar_button = tk.Button(ventana, text="Explicar", command=lambda: explicar(regex_entry.get(), explanation_display))
    explicar_button.pack()

    ventana.mainloop()

def validar(regex, cadenas, resultado_text):
    resultado_text.delete(1.0, tk.END)  # Limpiar el área de resultado
    try:
        compiled_regex = re.compile(regex)  # Compilar la expresión regular para verificar su validez
    except re.error:
        resultado_text.insert(tk.END, "Expresión regular inválida.\n")
        return

    cadenas = cadenas.split(',')  # Separar las cadenas por comas

    for cadena in cadenas:
        cadena = cadena.strip()  # Limpiar espacios
        if compiled_regex.fullmatch(cadena):
            resultado_text.insert(tk.END, f"{cadena}: Aceptada\n")
        else:
            resultado_text.insert(tk.END, f"{cadena}: Rechazada\n")

def resaltar(regex, highlighted_label):
    resaltado = resaltar_sintaxis(regex)  # Obtener el resaltado como cadena
    highlighted_label.config(text=resaltado)  # Actualizar el texto del label

def explicar(regex, explanation_display):
    explanation_display.config(text=explicar_regex(regex))  # Mostrar la explicación en el Label

if __name__ == "__main__":
    crear_interfaz()
