import random
import time
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ---------------- ALGORITMOS DE ORDENAMIENTO ----------------
def bubblesort(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def mergesort(lista):
    lista = lista.copy()
    def merge_sort(lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            L = lst[:mid]
            R = lst[mid:]

            merge_sort(L)
            merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    lst[k] = L[i]
                    i += 1
                else:
                    lst[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                lst[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                lst[k] = R[j]
                j += 1
                k += 1
    merge_sort(lista)
    return lista

def quicksort(lista):
    lista = lista.copy()
    def quick_sort(lst):
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst[0]
            left = [x for x in lst[1:] if x <= pivot]
            right = [x for x in lst[1:] if x > pivot]
            return quick_sort(left) + [pivot] + quick_sort(right)
    return quick_sort(lista)

# ---------------- GENERADOR Y MEDIDOR DE TIEMPO ----------------
def generar_lista(N):
    return [random.randint(1, 1000) for _ in range(N)]

def medir_tiempo(algoritmo, lista):
    inicio = time.perf_counter()
    algoritmo(lista)
    fin = time.perf_counter()
    return (fin - inicio) * 1000  # en milisegundos

# ---------------- COMPARADOR Y GRAFICADOR ----------------
def comparar_algoritmos():
    tamanios = list(range(50, 1050, 50))
    tiempos_bubble = []
    tiempos_merge = []
    tiempos_quick = []

    for n in tamanios:
        lista = generar_lista(n)
        tiempos_bubble.append(medir_tiempo(bubblesort, lista))
        tiempos_merge.append(medir_tiempo(mergesort, lista))
        tiempos_quick.append(medir_tiempo(quicksort, lista))

    graficar(tamanios, tiempos_bubble, tiempos_merge, tiempos_quick)

def graficar(tamanios, tiempos_bubble, tiempos_merge, tiempos_quick):
    # Limpia el contenido anterior si existe
    for widget in frame_grafica.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(8, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(tamanios, tiempos_bubble, label='Bubble Sort', color=(1.0, 0.5, 0.0))  # naranja (RGB)
    ax.plot(tamanios, tiempos_merge, label='Merge Sort', color=(0.0, 0.0, 1.0))    # azul
    ax.plot(tamanios, tiempos_quick, label='Quick Sort', color=(0.0, 0.7, 0.0))    # verde oscuro
    ax.set_title('Comparación de Algoritmos de Ordenamiento')
    ax.set_xlabel('Tamaño de la lista')
    ax.set_ylabel('Tiempo de ejecución (ms)')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack()

# ---------------- GUI ----------------
ventana = tk.Tk()
ventana.title("Comparador de Algoritmos de Ordenamiento")
ventana.geometry("900x700")

frame_grafica = tk.Frame(ventana)
frame_grafica.pack(fill=tk.BOTH, expand=True)

comparar_algoritmos()

ventana.mainloop()
