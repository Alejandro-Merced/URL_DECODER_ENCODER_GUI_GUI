import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica
from tkinter import scrolledtext  # Importa el widget ScrolledText para el área de texto con desplazamiento
from urllib.parse import quote, unquote  # Importa las funciones quote y unquote para codificar y decodificar URLs

# Función para codificar el texto
def encode():
    unencoded = text_area.get("1.0", tk.END).strip()  # Obtiene el texto del área de texto y elimina espacios en blanco
    encoded = quote(unencoded, safe='')  # Codifica el texto usando quote
    text_area.delete("1.0", tk.END)  # Borra el contenido actual del área de texto
    text_area.insert(tk.END, encoded)  # Inserta el texto codificado en el área de texto

# Función para decodificar el texto
def decode():
    encoded = text_area.get("1.0", tk.END).strip()  # Obtiene el texto codificado del área de texto y elimina espacios en blanco
    decoded = unquote(encoded)  # Decodifica el texto usando unquote
    text_area.delete("1.0", tk.END)  # Borra el contenido actual del área de texto
    text_area.insert(tk.END, decoded)  # Inserta el texto decodificado en el área de texto

# Funciones para el menú contextual
def copy():
    root.clipboard_clear()
    root.clipboard_append(text_area.selection_get())

def paste():
    text_area.insert(tk.INSERT, root.clipboard_get())

def create_context_menu(event):
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(label="Copy", command=copy)
    context_menu.add_command(label="Paste", command=paste)
    context_menu.post(event.x_root, event.y_root)

# Crear la ventana principal
root = tk.Tk()  # Crea una instancia de la ventana principal
root.title("URL Encoder/Decoder")  # Establece el título de la ventana

# Crear un label con instrucciones
instructions = tk.Label(root, text="Pega el enlace en el cuadro de texto y usa los botones para codificar o decodificar. Después puede copiar el texto modificado")
instructions.pack(padx=10, pady=5)  # Empaqueta el label en la ventana principal con padding

# Crear el área de texto con desplazamiento
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)  # Crea un widget ScrolledText
text_area.pack(padx=10, pady=10)  # Empaqueta el widget en la ventana principal con padding

# Asociar el menú contextual al área de texto
text_area.bind("<Button-3>", create_context_menu)

# Crear los botones
encode_button = tk.Button(root, text="Encode", command=encode)  # Crea un botón para codificar el texto
encode_button.pack(side=tk.LEFT, padx=10, pady=10)  # Empaqueta el botón en el lado izquierdo con padding

decode_button = tk.Button(root, text="Decode", command=decode)  # Crea un botón para decodificar el texto
decode_button.pack(side=tk.RIGHT, padx=10, pady=10)  # Empaqueta el botón en el lado derecho con padding

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()  # Inicia el bucle principal de la interfaz gráfica
