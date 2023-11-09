import tkinter as tk

window = tk.Tk("Metodos numericos")
window.title('Metodos numericos')

appTitle = tk.Message(window, text='Bienvenido a metodos numericos!!')
appTitle.pack()

buttonCeros = tk.Button(window, text='Ceros', width=25)
buttonCeros.pack()

buttonInterpolacion = tk.Button(window, text='Interpolación', width=25)
buttonInterpolacion.pack()

buttonEDO1 = tk.Button(window, text='Ecuaciones Diferenciales Ordinarias de orden 1', width=35)
buttonEDO1.pack()

window.mainloop()