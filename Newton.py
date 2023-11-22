
import tkinter as tk
from metodos import NewtonR
import sympy as sp

class newtonApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_newton()

    def mostrar_newton(self):
        pregunta_label = tk.Label(self.ventana, text="Ingresa la funcion:")
        pregunta_label.pack()
        funcion = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        funcion.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa x0:")
        pregunta_label.pack()
        x0 = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        x0.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa tolerancia:")
        pregunta_label.pack()
        tol = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        tol.pack() 

        boton_verificar = tk.Button(self.ventana, text="Calcular", command=lambda: self.Calcular(resultado_label, iteraciones_label, funcion.get("1.0","end-1c"), x0.get("1.0","end-1c"), tol.get("1.0","end-1c")))
        boton_verificar.pack()


        resultadotxt = tk.Label(self.ventana, text= "Solucion")
        resultadotxt.pack()
        resultado_label = tk.Label(self.ventana, text= "")
        resultado_label.pack()

        iteracionestxt = tk.Label(self.ventana, text= "Numero de Iteraciones")
        iteracionestxt.pack()
        iteraciones_label = tk.Label(self.ventana, text= "")
        iteraciones_label.pack()

    def Calcular(self,resultado_label, iteraciones_label, f, x0, tol):
        raiz, iteraciones = NewtonR(f,x0,tol)
        resultado_label.config(text = raiz)
        iteraciones_label.config(text = iteraciones)


if __name__ == "__main__":
    ventana_newton = tk.Tk()
    app_newton = newtonApp(ventana_newton)
    ventana_newton.mainloop()