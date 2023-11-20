import tkinter as tk
from tkinter import messagebox
import Ceros
import Interpolacion
import Edo1
import Edo2
import Integracion

def desmontar(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def verificar_respuesta(eleccion, ventana):
    desmontar(ventana)
    match eleccion:
        case 1:
            return Ceros.Ceros(ventana)
        case 2:
            Interpolacion.Interpolacion(ventana)
        case 3:
            Edo1.Edo1(ventana)
        case 4:
            Edo2.Edo2(ventana)
        case 5:
            Integracion.Integracion(ventana)

def main():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Metodos numericos")

    # Pregunta
    pregunta_label = tk.Label(ventana, text="¿Que metodo desea utilizar?")
    pregunta_label.pack()

    # Opciones de selección múltiple
    eleccion = tk.IntVar()
    opcion1 = tk.Radiobutton(ventana, text="Ceros", variable=eleccion, value=1)
    opcion2 = tk.Radiobutton(ventana, text="Interpolación", variable=eleccion, value=2)
    opcion3 = tk.Radiobutton(ventana, text="Ecuaciones Diferenciales Orden 1", variable=eleccion, value=3)
    opcion4 = tk.Radiobutton(ventana, text="Ecuaciones Diferenciales Orden 2", variable=eleccion, value=4)
    opcion5 = tk.Radiobutton(ventana, text="Integracion", variable=eleccion, value=5)

    opcion1.pack()
    opcion2.pack()
    opcion3.pack()
    opcion4.pack()
    opcion5.pack()

    # Botón para verificar la respuesta
    boton_verificar = tk.Button(ventana, text="Siguiente", command=lambda: verificar_respuesta(eleccion.get(), ventana))
    boton_verificar.pack()

    # Ejecutar el bucle principal
    ventana.mainloop()

if __name__ == "__main__":
    main()
