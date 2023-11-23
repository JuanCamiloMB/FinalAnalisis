import tkinter as tk
from metodos import Simpson13_Simple

class s38App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.mostrar_s38()

    def mostrar_s38(self):
        pregunta_label = tk.Label(self.ventana, text="Ingresa la funcion:")
        pregunta_label.pack()
        funcion = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        funcion.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa Limite inferior:")
        pregunta_label.pack()
        lim_inf = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        lim_inf.pack()

        pregunta_label = tk.Label(self.ventana, text="Ingresa Limite superior:")
        pregunta_label.pack()
        lim_sup = tk.Text(self.ventana, height = 10,
                width = 25,
                bg = "light yellow")
        lim_sup.pack() 

        boton_verificar = tk.Button(self.ventana, text="Calcular", command=lambda: self.Calcular(resultado_label, funcion.get("1.0","end-1c"), lim_inf.get("1.0","end-1c"), lim_sup.get("1.0","end-1c")))
        boton_verificar.pack()


        resultadotxt = tk.Label(self.ventana, text= "Solucion")
        resultadotxt.pack()
        resultado_label = tk.Label(self.ventana, text= "")
        resultado_label.pack()

    def Calcular(self,resultado_label, f, lim_inf, lim_sup):
        raiz = Simpson13_Simple(f,lim_inf, lim_sup)
        resultado_label.config(text = raiz)


if __name__ == "__main__":
    ventana_t = tk.Tk()
    app_s38 = s38App(ventana_t)
    ventana_t.mainloop()