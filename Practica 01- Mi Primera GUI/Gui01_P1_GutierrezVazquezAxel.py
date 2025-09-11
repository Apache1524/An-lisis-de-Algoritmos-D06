import tkinter as tk
from colorama import Fore, Back, Style, init
init() 

root = tk.Tk()
root.title("Yo soy ese :hola mundo")
root.geometry("720x450")
def cambiar_color():
    lbl.config(fg="red")
    lbl2.config(fg="blue")

lbl = tk.Label(root, text="kiubo, ¿como estas?")
lbl.pack(pady=80)

lbl2 = tk.Label(root, text="nO leas esto :u")
lbl2.pack(pady=45)

boton_cambiar = tk.Button(root, text="swish color", command=cambiar_color)
boton_cambiar.pack()


root.mainloop()

