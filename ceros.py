import tkinter as tk
import Newton
import Secante
import Biseccion
import FalsaPosicion

def desmontar(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def verificar_respuesta(eleccion, ventana):
    desmontar(ventana)
    match eleccion:
        case 1:
            Newton.Newton(ventana)
        case 2:
            Secante.Secante(ventana)
        case 3:
            Biseccion.Biseccion(ventana)
        case 4:
            FalsaPosicion.FalsaPosicion(ventana)

def Ceros(ventana):
    pregunta_label = tk.Label(ventana, text="Metodos de ceros:")
    pregunta_label.pack()

    eleccion = tk.IntVar()
    opcion1 = tk.Radiobutton(ventana, text="Newton", variable=eleccion, value=1)
    opcion2 = tk.Radiobutton(ventana, text="Secante", variable=eleccion, value=2)
    opcion3 = tk.Radiobutton(ventana, text="Biseccion", variable=eleccion, value=3)
    opcion4 = tk.Radiobutton(ventana, text="Falsa Posicion", variable=eleccion, value=4)
    
    opcion1.pack()
    opcion2.pack()
    opcion3.pack()
    opcion4.pack()

    boton_verificar = tk.Button(ventana, text="Siguiente", command=lambda: verificar_respuesta(eleccion, ventana))
    boton_verificar.pack()

if __name__ == "__ceros__":
    Ceros()