import tkinter as tk
from tkinter import messagebox
import Euler
import Runge
import main

class Edo1App:
    def __init__(self, ventana, volver_a_inicio):
        self.ventana = ventana
        self.volver_a_inicio = volver_a_inicio
        self.mostrar_edo1()

    def desmontar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def verificar_respuesta(self, eleccion):
        if eleccion == 0:
            messagebox.showerror("Error", "Seleccione una opción")
        else:
            self.desmontar()
            if eleccion == 1:
                Euler.eulerApp(self.ventana)
            elif eleccion == 2:
                Runge.Runge(self.ventana)

    def mostrar_edo1(self):
        pregunta_label = tk.Label(self.ventana, text="Métodos de EDO1:")
        pregunta_label.pack()

        eleccion = tk.IntVar()
        opcion1 = tk.Radiobutton(self.ventana, text="Euler", variable=eleccion, value=1)
        opcion2 = tk.Radiobutton(self.ventana, text="Runge", variable=eleccion, value=2)

        opcion1.pack()
        opcion2.pack()

        boton_verificar = tk.Button(self.ventana, text="Siguiente", command=lambda: self.verificar_respuesta(eleccion.get()))
        boton_verificar.pack()

        boton_atras = tk.Button(self.ventana, text="Atrás", command=self.volver_a_inicio)
        boton_atras.pack()

if __name__ == "__edo1__":
    ventana_edo1 = tk.Tk()
    app_edo1 = Edo1App(ventana_edo1, main)
    ventana_edo1.mainloop()
