import tkinter as tk

def cambiar_color():
    lbl.config(fg="RED")

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "buscando ando"
    lbl.config(text=f"Salu2, {nombre} 🤞😉")

root = tk.Tk()
root.title("Saludador de skibidiCompadres")
root.geometry("500x750")

lbl = tk.Label(root, text="🗣Oye morty, escribe tu nombre y dale al boton, la recompensa es GRANDE!!🥒")
lbl.pack(pady=15)

entrada = tk.Entry(root)
entrada.pack(pady=6)

btn = tk.Button(root, text="salu2 aqui", command=saludar)
btn.pack(pady=10)

boton_cambiar = tk.Button(root, text="DALE AL BOTON MORTY VAMOS", command=cambiar_color)
boton_cambiar.pack()

root.mainloop()

