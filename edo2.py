import tkinter as tk
from tkinter import messagebox
import Euler
import Runge
import main

class Edo2App:
    def __init__(self, ventana, volver_a_inicio):
        self.ventana = ventana
        self.volver_a_inicio = volver_a_inicio
        self.mostrar_edo2()

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
                Runge.rungeApp(self.ventana)

    def mostrar_edo2(self):
        pregunta_label = tk.Label(self.ventana, text="Métodos de EDO2:")
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

if __name__ == "__edo2__":
    ventana_edo2 = tk.Tk()
    app_edo2 = Edo2App(ventana_edo2, main)
    ventana_edo2.mainloop()
