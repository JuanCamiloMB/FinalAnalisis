import tkinter as tk
from tkinter import messagebox
import main
import T
import S1_3
import S3_8

class IntegracionApp:
    def __init__(self, ventana, volver_a_inicio):
        self.ventana = ventana
        self.volver_a_inicio = volver_a_inicio
        self.mostrar_integracion()

    def desmontar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def verificar_respuesta(self, eleccion):
        if eleccion == 0:
            messagebox.showerror("Error", "Seleccione una opción")
        else:
            self.desmontar()
            # Lógica adicional para manejar la respuesta del usuario si es necesario
            if eleccion == 1:
                T.T(self.ventana)
            elif eleccion == 2:
                S1_3.S1_3(self.ventana)
            elif eleccion == 3:
                S3_8.S3_8(self.ventana)

    def mostrar_integracion(self):
        pregunta_label = tk.Label(self.ventana, text="Metodos de integracion:")
        pregunta_label.pack()

        eleccion = tk.IntVar()
        opcion1 = tk.Radiobutton(self.ventana, text="T", variable=eleccion, value=1)
        opcion2 = tk.Radiobutton(self.ventana, text="s1/3", variable=eleccion, value=2)
        opcion3 = tk.Radiobutton(self.ventana, text="s3/8", variable=eleccion, value=3)

        opcion1.pack()
        opcion2.pack()
        opcion3.pack()

        boton_verificar = tk.Button(self.ventana, text="Siguiente", command=lambda: self.verificar_respuesta(eleccion.get()))
        boton_verificar.pack()

        boton_atras = tk.Button(self.ventana, text="Atrás", command=self.volver_a_inicio)
        boton_atras.pack()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = IntegracionApp(ventana, main.MainApp)
    ventana.mainloop()

