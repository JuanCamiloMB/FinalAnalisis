import tkinter as tk
import numpy as np

class secanteApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_secante()

    def mostrar_secante(self):
        pregunta_label = tk.Label(self.ventana, text="Ingresa la funcion (en Python):")
        pregunta_label.pack()
        funcion = tk.Entry(self.ventana, bg="light yellow")
        funcion.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa x0:")
        pregunta_label.pack()
        x0 = tk.Entry(self.ventana, bg="light yellow")
        x0.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa x1:")
        pregunta_label.pack()
        x1 = tk.Entry(self.ventana, bg="light yellow")
        x1.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa tolerancia:")
        pregunta_label.pack()
        tol = tk.Entry(self.ventana, bg="light yellow")
        tol.pack()

        resultado_label = tk.Label(self.ventana, text="")
        resultado_label.pack()

        boton_verificar = tk.Button(self.ventana, text="Calcular", command=lambda: self.Calcular(resultado_label, funcion.get(), float(x0.get()), float(x1.get()), float(tol.get())))
        boton_verificar.pack()

    def Calcular(self, resultado_label, f, x0, x1, tol):
        # Convertir la cadena de texto a una función lambda
        f_lambda = lambda x: eval(f)

        x2 = x1 - f_lambda(x1) * (x0 - x1) / (f_lambda(x0) - f_lambda(x1))

        while np.abs(x2 - x1) > tol:
            x0 = x1
            x1 = x2
            x2 = x1 - f_lambda(x1) * (x0 - x1) / (f_lambda(x0) - f_lambda(x1))

        resultado_label.config(text=f'La raiz de la funcion {f} por el metodo secante es: {x2}')

if __name__ == "__main__":
    ventana_secante = tk.Tk()
    app_secante = secanteApp(ventana_secante)
    ventana_secante.mainloop()



