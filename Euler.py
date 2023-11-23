import tkinter as tk
from metodos import Euler

class eulerApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_euler()

    def mostrar_euler(self):
        pregunta_label = tk.Label(self.ventana, text="Ingresa la funcion (con variables t,y):")
        pregunta_label.pack()
        funcion = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        funcion.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa limite inferior:")
        pregunta_label.pack()
        lim_inf = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        lim_inf.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa limite superior:")
        pregunta_label.pack()
        lim_sup = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        lim_sup.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa h:")
        pregunta_label.pack()
        h = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        h.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa Condicion inicial:")
        pregunta_label.pack()
        exactitud = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        exactitud.pack() 

        boton_verificar = tk.Button(self.ventana, text="Calcular", command=lambda: self.Calcular(resultado_label, funcion.get("1.0","end-1c"), lim_inf.get("1.0","end-1c"), lim_sup.get("1.0","end-1c"), h.get("1.0","end-1c"),exactitud.get("1.0","end-1c")))
        boton_verificar.pack()


        resultadotxt = tk.Label(self.ventana, text= "Solucion")
        resultadotxt.pack()
        resultado_label = tk.Label(self.ventana, text= "")
        resultado_label.pack()

    def Calcular(self,resultado_label, f, lim_inf, lim_sup, h, exactitud):
        raiz = Euler(f,lim_inf, lim_sup, h, exactitud)
        resultado_label.config(text = raiz)


if __name__ == "__main__":
    ventana_euler = tk.Tk()
    app_euler = eulerApp(ventana_euler)
    ventana_euler.mainloop()