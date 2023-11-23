import tkinter as tk
import numpy as np
import sympy as sp
from metodos import lagrange

class LagrangeApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_lagrange()

    def mostrar_lagrange(self):
        pregunta_label = tk.Label(self.ventana, text="Ingresa los valores de xi (separados por comas):")
        pregunta_label.pack()
        xi = tk.Entry(self.ventana, bg="light yellow")
        xi.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa los valores de fxi (separados por comas):")
        pregunta_label.pack()
        fxi = tk.Entry(self.ventana, bg="light yellow")
        fxi.pack()

        resultado_label = tk.Label(self.ventana, text="")
        resultado_label.pack()

        boton_verificar = tk.Button(self.ventana, text="Calcular", command=lambda: self.Calcular(resultado_label, xi.get(), fxi.get()))
        boton_verificar.pack()

    def Calcular(self, resultado_label, xi, fxi):
        xi = np.array([float(x) for x in xi.split(",")])
        fxi = np.array([float(x) for x in fxi.split(",")])

        polinomio = lagrange(xi, fxi)
        resultado_label.config(text=f'El polinomio es P(X): {polinomio(sp.symbols("X"))}')

if __name__ == "__main__":
    ventana_lagrange = tk.Tk()
    app_lagrange = LagrangeApp(ventana_lagrange)
    ventana_lagrange.mainloop()
