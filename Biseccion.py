import tkinter as tk
from metodos import Biseccion

class biseccionApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_biseccion()

    def mostrar_biseccion(self):
        pregunta_label = tk.Label(self.ventana, text="Ingresa la funcion (en Python):")
        pregunta_label.pack()
        funcion = tk.Entry(self.ventana, bg="light yellow")
        funcion.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa limite inferior:")
        pregunta_label.pack()
        lim_inf = tk.Entry(self.ventana, bg="light yellow")
        lim_inf.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa limite superior:")
        pregunta_label.pack()
        lim_sup = tk.Entry(self.ventana, bg="light yellow")
        lim_sup.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa exactitud:")
        pregunta_label.pack()
        exactitud = tk.Entry(self.ventana, bg="light yellow")
        exactitud.pack()

        resultado_label = tk.Label(self.ventana, text="")
        resultado_label.pack()

        boton_verificar = tk.Button(self.ventana, text="Calcular", command=lambda: self.Calcular(resultado_label, funcion.get(), float(lim_inf.get()), float(lim_sup.get()), float(exactitud.get())))
        boton_verificar.pack()

    def Calcular(self, resultado_label, f, lim_inf, lim_sup, exactitud):
        # Convertir la cadena de texto a una función lambda
        f_lambda = lambda x: eval(f)

        result = Biseccion(f_lambda, lim_inf, lim_sup, exactitud)
        resultado_label.config(text=f'La raiz de la funcion {f} es: {result}')

if __name__ == "__main__":
    ventana_biseccion = tk.Tk()
    app_biseccion = biseccionApp(ventana_biseccion)
    ventana_biseccion.mainloop()

