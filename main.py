import tkinter as tk
from tkinter import messagebox
import ceros
import interpolacion
import edo1
import edo2
import integracion

class MainApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Metodos numericos")
        self.mostrar_inicio()

    def desmontar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def volver_a_inicio(self):
        self.desmontar()
        self.mostrar_inicio()

    def mostrar_inicio(self):
        # Pregunta
        pregunta_label = tk.Label(self.ventana, text="¿Qué método desea utilizar?")
        pregunta_label.pack()

        # Opciones de selección múltiple
        eleccion = tk.IntVar()
        opcion1 = tk.Radiobutton(self.ventana, text="Ceros", variable=eleccion, value=1)
        opcion2 = tk.Radiobutton(self.ventana, text="Interpolación", variable=eleccion, value=2)
        opcion3 = tk.Radiobutton(self.ventana, text="Ecuaciones Diferenciales Orden 1", variable=eleccion, value=3)
        opcion4 = tk.Radiobutton(self.ventana, text="Ecuaciones Diferenciales Orden 2", variable=eleccion, value=4)
        opcion5 = tk.Radiobutton(self.ventana, text="integracion", variable=eleccion, value=5)

        opcion1.pack()
        opcion2.pack()
        opcion3.pack()
        opcion4.pack()
        opcion5.pack()

        # Botón para verificar la respuesta
        boton_verificar = tk.Button(self.ventana, text="Siguiente", command=lambda: self.verificar_respuesta(eleccion.get()))
        boton_verificar.pack()

    def verificar_respuesta(self, eleccion):
        if eleccion == 0:
            messagebox.showerror("Error", "Seleccione una opción")
        else:
            self.desmontar()
            if eleccion == 1:
                ceros.CerosApp(self.ventana, self.volver_a_inicio)
            elif eleccion == 2:
                interpolacion.InterpolacionApp(self.ventana, self.volver_a_inicio)
            elif eleccion == 3:
                edo1.Edo1App(self.ventana, self.volver_a_inicio)
            elif eleccion == 4:
                edo2.Edo2App(self.ventana, self.volver_a_inicio)
            elif eleccion == 5:
                integracion.IntegracionApp(self.ventana, self.volver_a_inicio)

def main():
    ventana = tk.Tk()
    app = MainApp(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()


