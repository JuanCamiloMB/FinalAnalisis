import tkinter as tk
from metodos import MC
import numpy as np

class MinimosCuadradosApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_minimos_cuadrados()

    def mostrar_minimos_cuadrados(self):
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

        a0, a1 = MC(xi, fxi)
        resultado_label.config(text=f'Los coeficientes a0 y a1 son: {a0}, {a1}')

if __name__ == "__main__":
    ventana_minimos_cuadrados = tk.Tk()
    app_minimos_cuadrados = MinimosCuadradosApp(ventana_minimos_cuadrados)
    ventana_minimos_cuadrados.mainloop()
