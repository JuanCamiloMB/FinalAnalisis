import tkinter as tk
from tkinter import messagebox
import Newton
import Secante
import Biseccion
import FalsaPosicion
import main

class CerosApp:
    def __init__(self, ventana, volver_a_inicio):
        self.ventana = ventana
        self.volver_a_inicio = volver_a_inicio
        self.mostrar_ceros()

    def desmontar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def verificar_respuesta(self, eleccion):
        if eleccion == 0:
            messagebox.showerror("Error", "Seleccione una opción")
        else:
            self.desmontar()
            if eleccion == 1:
                Newton.newtonApp(self.ventana)
            elif eleccion == 2:
                Secante.secanteApp(self.ventana)
            elif eleccion == 3:
                Biseccion.biseccionApp(self.ventana)
            elif eleccion == 4:
                FalsaPosicion.falsaposicionApp(self.ventana)

    def mostrar_ceros(self):
        pregunta_label = tk.Label(self.ventana, text="Metodos de ceros:")
        pregunta_label.pack()

        eleccion = tk.IntVar()
        opcion1 = tk.Radiobutton(self.ventana, text="Newton", variable=eleccion, value=1)
        opcion2 = tk.Radiobutton(self.ventana, text="Secante", variable=eleccion, value=2)
        opcion3 = tk.Radiobutton(self.ventana, text="Biseccion", variable=eleccion, value=3)
        opcion4 = tk.Radiobutton(self.ventana, text="Falsa Posicion", variable=eleccion, value=4)

        opcion1.pack()
        opcion2.pack()
        opcion3.pack()
        opcion4.pack()

        boton_verificar = tk.Button(self.ventana, text="Siguiente", command=lambda: self.verificar_respuesta(eleccion.get()))
        boton_verificar.pack()

        boton_atras = tk.Button(self.ventana, text="Atrás", command=self.volver_a_inicio)
        boton_atras.pack()

if __name__ == "__main__":
    ventana_ceros = tk.Tk()
    app_ceros = CerosApp(ventana_ceros, main)
    ventana_ceros.mainloop()

