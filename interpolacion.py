import tkinter as tk
from tkinter import messagebox
import Lagrange
import MinimosCuadrados
import PolinomialSimple
import main

class InterpolacionApp:
    def __init__(self, ventana, volver_a_inicio):
        self.ventana = ventana
        self.volver_a_inicio = volver_a_inicio
        self.mostrar_interpolacion()

    def desmontar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def verificar_respuesta(self, eleccion):
        if eleccion == 0:
            messagebox.showerror("Error", "Seleccione una opción")
        else:
            self.desmontar()
            if eleccion == 1:
                Lagrange.Lagrange(self.ventana)
            elif eleccion == 2:
                MinimosCuadrados.MinimosCuadrados(self.ventana)
            elif eleccion == 3:
                PolinomialSimple.PolinomialSimple(self.ventana)

    def mostrar_interpolacion(self):
        # Pregunta
        pregunta_label = tk.Label(self.ventana, text="¿Qué método de interpolación desea utilizar?")
        pregunta_label.pack()

        # Opciones de selección múltiple
        eleccion = tk.IntVar()
        opcion1 = tk.Radiobutton(self.ventana, text="Lagrange", variable=eleccion, value=1)
        opcion2 = tk.Radiobutton(self.ventana, text="Mínimos cuadrados", variable=eleccion, value=2)
        opcion3 = tk.Radiobutton(self.ventana, text="Polinomial simple", variable=eleccion, value=3)

        opcion1.pack()
        opcion2.pack()
        opcion3.pack()

        # Botón para verificar la respuesta
        boton_verificar = tk.Button(self.ventana, text="Siguiente", command=lambda: self.verificar_respuesta(eleccion.get()))
        boton_verificar.pack()

        # Botón para volver atrás
        boton_atras = tk.Button(self.ventana, text="Atrás", command=self.volver_a_inicio)
        boton_atras.pack()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterpolacionApp(ventana, main)
    ventana.mainloop()

