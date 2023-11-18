import tkinter as tk

def desmontar(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def verificar_respuesta(eleccion, ventana):
    respuesta_usuario = eleccion.get()
    desmontar(ventana)

def integracion(ventana):
    pregunta_label = tk.Label(ventana, text="Metodos de integracion:")
    pregunta_label.pack()

    eleccion = tk.IntVar()
    opcion1 = tk.Radiobutton(ventana, text="T", variable=eleccion, value=1)
    opcion2 = tk.Radiobutton(ventana, text="s1/3", variable=eleccion, value=2)
    opcion3 = tk.Radiobutton(ventana, text="s3/8", variable=eleccion, value=3)

    boton_verificar = tk.Button(ventana, text="Verificar", command=lambda: verificar_respuesta(eleccion, ventana))
    boton_verificar.pack()

if __name__ == "__integracion__":
    integracion()