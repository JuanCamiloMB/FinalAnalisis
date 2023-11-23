import tkinter as tk
import numpy as np
import sympy as sp
from metodos import p_simple

class PolinomialSimpleApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_polinomial_simple()

    def mostrar_polinomial_simple(self):
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

        polinomio = p_simple(xi, fxi)
        if polinomio is not None:
            resultado_label.config(text=f'El polinomio interpolante es: P(X) = {polinomio(sp.symbols("X"))}')
        else:
            resultado_label.config(text='Error: La matriz es singular')

if __name__ == "__main__":
    ventana_polinomial_simple = tk.Tk()
    app_polinomial_simple = PolinomialSimpleApp(ventana_polinomial_simple)
    ventana_polinomial_simple.mainloop()
