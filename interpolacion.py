import tkinter as tk
import Lagrange
import MinimosCuadrados
import PolinomialSimple

def desmontar(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def verificar_respuesta(eleccion, ventana):
    desmontar(ventana)
    match eleccion:
        case 1:
            Lagrange.Lagrange(ventana)
        case 2:
            MinimosCuadrados.MinimosCuadrados(ventana)
        case 3:
            PolinomialSimple.PolinomialSimple(ventana)

def Interpolacion(ventana):
    pregunta_label = tk.Label(ventana, text="Metodos de interpolacion:")
    pregunta_label.pack()

    eleccion = tk.IntVar()
    opcion1 = tk.Radiobutton(ventana, text="Lagrange", variable=eleccion, value=1)
    opcion2 = tk.Radiobutton(ventana, text="Minimos cuadrados", variable=eleccion, value=2)
    opcion3 = tk.Radiobutton(ventana, text="Polinomial simple", variable=eleccion, value=3)

    opcion1.pack()
    opcion2.pack()
    opcion3.pack()

    boton_verificar = tk.Button(ventana, text="Siguiente", command=lambda: verificar_respuesta(eleccion, ventana))
    boton_verificar.pack()

if __name__ == "__interpolacion__":
    Interpolacion()