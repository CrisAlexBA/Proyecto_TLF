from automata import AFD
from lector import Lector
from analizadorSintactico import AnalizadorSintactico
import tkinter
from PIL import Image, ImageTk
import os


def construir_automata(regex):
    """
    Construye un Automata a partir de la expresión regular.
    """
    try:
        # Paso 1: Tokenizar la expresión regular
        print("Tokenizando la expresión regular...")
        reader = Lector(regex)
        tokens = reader.crear_tokens()

        # Paso 2: Construir el árbol sintáctico
        print("Construyendo el árbol sintáctico...")
        parser = AnalizadorSintactico(tokens)
        syntax_tree = parser.Analizar()

        # Validar el árbol sintáctico
        if not syntax_tree:
            raise ValueError("El árbol sintáctico no se generó correctamente.")

        # Paso 3: Obtener los símbolos de la expresión regular
        print("Obteniendo símbolos de la expresión regular...")
        symbols = reader.obtener_simbolos()

        # Paso 4: Construir el AFD
        print("Construyendo el AFD...")
        afd = AFD(syntax_tree, symbols, regex)

        # Paso 5: Generar el gráfico
        print("Generando el gráfico del AFD...")
        afd.graficar_AFD()
        output_path = './output/AFD.png'


        print("AFD construido correctamente.")
        return output_path

    except Exception as e:
        print(f"Error al construir el AFD: {e}")
        return None


def mostrar_ventana_automata(ruta_imagen):
    """
    Muestra la imagen del autómata generado en una ventana de Tkinter.
    """
    ventana = tkinter.Toplevel()  # Usamos Toplevel para no bloquear la ventana principal
    ventana.title("Visualización del AFD")
    ventana.geometry("600x500")

    try:
        # Verificar si la imagen existe
        if not os.path.exists(ruta_imagen):
            tkinter.messagebox.showerror("Error", f"La imagen no existe en la ruta: {ruta_imagen}")
            return

        # Cargar la imagen
        img = Image.open(ruta_imagen)
        img_tk = ImageTk.PhotoImage(img)

        # Mantener la referencia de la imagen
        ventana.img_tk = img_tk  # Guardamos la imagen en un atributo de la ventana

        # Crear un widget de etiqueta para mostrar la imagen
        etiqueta = tkinter.Label(ventana, image=img_tk)
        etiqueta.pack()

        # Ejecutar la ventana
        ventana.mainloop()

    except Exception as e:
        tkinter.messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
