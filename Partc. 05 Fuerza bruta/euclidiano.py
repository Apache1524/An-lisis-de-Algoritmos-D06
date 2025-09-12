import math
import random
import tkinter as tk
from tkinter import scrolledtext
import threading

Puntos = []
Dist = []

def llenarPuntos(cantidad=5):
    Puntos.clear()
    Dist.clear()
    for i in range(cantidad):
        x = random.randint(0, 40)
        y = random.randint(0, 40)
        Puntos.append((x, y))
        x_entries[i].delete(0, tk.END)
        x_entries[i].insert(0, str(x))
        y_entries[i].delete(0, tk.END)
        y_entries[i].insert(0, str(y))
    print("\nPuntos generados:")
    resultadosText.insert(tk.END, "\nPuntos generados:\n")
    for i, (x, y) in enumerate(Puntos, 1):
        linea = f"P{i} = ({x}, {y})"
        print(linea)
        resultadosText.insert(tk.END, linea + "\n")

def capturarPuntos(cantidad=5):
    Puntos.clear()
    Dist.clear()
    for i in range(cantidad):
        x = float(x_entries[i].get())
        y = float(y_entries[i].get())
        Puntos.append((x, y))
    return True

def calcularComparacion():
    resultadosText.delete("1.0", tk.END)
    ok = capturarPuntos()
    if not ok:
        return
    for i in range(len(Puntos)):
        for j in range(i+1, len(Puntos)):
            x1, y1 = Puntos[i]
            x2, y2 = Puntos[j]
            d = math.hypot(x2 - x1, y2 - y1)
            Dist.append(d)
            linea = f"d = sqrt(({x2}-{x1})^2 + ({y2}-{y1})^2) = {d:.2f}"
            resultadosText.insert(tk.END, linea + "\n")
            print(linea)
    if Dist:
        min_dist = f"Distancia minima: {min(Dist):.2f}"
        max_dist = f"Distancia maxima: {max(Dist):.2f}"
        resultadosText.insert(tk.END, "\n" + min_dist + "\n")
        resultadosText.insert(tk.END, max_dist + "\n")
        print("\n" + min_dist)
        print(max_dist)
    else:
        msg = "No se calcularon distancias"
        resultadosText.insert(tk.END, msg + "\n")
        print(msg)

def limpiarPuntos():
    Puntos.clear()
    Dist.clear()
    for e in x_entries + y_entries:
        e.delete(0, tk.END)
    resultadosText.delete("1.0", tk.END)
    print("\nPuntos y resultados limpiados.")

def consolaLoop():
    while True:
        print("\nOpciones:")
        print("1 - Llenar puntos aleatorios")
        print("2 - Ingresar puntos manualmente")
        print("3 - Calcular distancias")
        print("4 - Limpiar puntos")
        print("0 - Salir")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            llenarPuntos()
        elif opcion == "2":
            Puntos.clear()
            for i in range(5):
                x = float(input(f"Ingrese X{i+1}: "))
                y = float(input(f"Ingrese Y{i+1}: "))
                Puntos.append((x, y))
            for i, (x, y) in enumerate(Puntos):
                x_entries[i].delete(0, tk.END)
                x_entries[i].insert(0, str(x))
                y_entries[i].delete(0, tk.END)
                y_entries[i].insert(0, str(y))
        elif opcion == "3":
            calcularComparacion()
        elif opcion == "4":
            limpiarPuntos()
        elif opcion == "0":
            print("Saliendo...")
            break

root = tk.Tk()
root.title("Comparador de Distancias - 5 Puntos")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Punto").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame, text="X").grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame, text="Y").grid(row=0, column=2, padx=5, pady=5)

x_entries = []
y_entries = []
for i in range(5):
    tk.Label(frame, text=f"P{i+1}").grid(row=i+1, column=0, padx=5, pady=3, sticky="w")
    ex = tk.Entry(frame, width=10)
    ey = tk.Entry(frame, width=10)
    ex.grid(row=i+1, column=1, padx=5, pady=3)
    ey.grid(row=i+1, column=2, padx=5, pady=3)
    x_entries.append(ex)
    y_entries.append(ey)

btn_frame = tk.Frame(frame)
btn_frame.grid(row=1, column=3, rowspan=5, padx=10)

btn_fill = tk.Button(btn_frame, text="Llenar", width=12, command=lambda: llenarPuntos(5))
btn_calc = tk.Button(btn_frame, text="Calcular", width=12, command=calcularComparacion)
btn_clear = tk.Button(btn_frame, text="Limpiar", width=12, command=limpiarPuntos)

btn_fill.pack(pady=5)
btn_calc.pack(pady=5)
btn_clear.pack(pady=5)

resultadosText = scrolledtext.ScrolledText(root, width=60, height=12)
resultadosText.pack(padx=10, pady=(5,10))

threading.Thread(target=consolaLoop, daemon=True).start()

root.mainloop()
