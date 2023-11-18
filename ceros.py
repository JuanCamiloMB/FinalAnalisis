import tkinter as tk

def desmontar(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def verificar_respuesta(eleccion, ventana):
    respuesta_usuario = eleccion.get()
    desmontar(ventana)

def ceros(ventana):
    pregunta_label = tk.Label(ventana, text="Metodos de ceros:")
    pregunta_label.pack()

    eleccion = tk.IntVar()
    opcion1 = tk.Radiobutton(ventana, text="Abierto", variable=eleccion, value=1)
    opcion2 = tk.Radiobutton(ventana, text="Cerrado", variable=eleccion, value=2)

    boton_verificar = tk.Button(ventana, text="Verificar", command=lambda: verificar_respuesta(eleccion, ventana))
    boton_verificar.pack()

if __name__ == "__ceros__":
    ceros()