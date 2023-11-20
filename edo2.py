import tkinter as tk
import Euler
import Runge

def desmontar(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def verificar_respuesta(eleccion, ventana):
    desmontar(ventana)
    match eleccion:
        case 1:
            Euler.Euler(ventana)
        case 2:
            Runge.Runge(ventana)


def Edo2(ventana):
    pregunta_label = tk.Label(ventana, text="Metodos de edo2:")
    pregunta_label.pack()

    eleccion = tk.IntVar()
    opcion1 = tk.Radiobutton(ventana, text="Euler", variable=eleccion, value=1)
    opcion2 = tk.Radiobutton(ventana, text="Runge", variable=eleccion, value=2)
    
    opcion1.pack()
    opcion2.pack()

    boton_verificar = tk.Button(ventana, text="Siguiente", command=lambda: verificar_respuesta(eleccion, ventana))
    boton_verificar.pack()

if __name__ == "__edo2__":
    Edo2()