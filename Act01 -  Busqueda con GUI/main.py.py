#importacion de librerias necesarias ---- （〃｀ 3′〃）   <--- Axel Gutierrez Vazquez

import random  #permite generar numero random
import time    #para medir el tiempo
import tkinter as tk   #libreria que permite la creacion de las GUI
from tkinter import ttk, messagebox #ttk para los widgets y messagebox para ventanas de error como cuando no se encuentre un numero
import numpy as np #libreria para calculos numericos, se utilizara para las barras en la grafica
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #para poner una grafica dentro de la misma ventana del GUI


#algoritmos de busqueda (lineal y binario) --- (。・ω・。)

def busqueda_lineal(lista, x):
    for i, value in enumerate(lista):  #enumerate para recorrer la lista de forma lineal hasta terminar
        if value == x:
            return i   #retorna el indice de la X si se encuentra el numero
    return -1  #retorna -1 si no se encuentra el numero

def busqueda_binaria(lista, x):
    izquierda = 0
    derecha = len(lista)- 1
    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        if lista[centro] == x:
            return centro  #retorna centro si su valor el igual al de X 
        elif lista[centro] < x:
            izquierda = centro +1
        else:
            derecha = centro -1
    return -1  #retorna -1 si no lo encuentra

#generamos los numeros aleatorios --- (￣﹃￣)  

def generar_lista_ordenada(size):
    universe = size * 10  #al multiplicarl el rango por 10 permitimos tener un rago de valores distintos mas alto
    sample = random.sample(range(universe),size)  #toma una cantidad (size) de numeros randoms distintos del rango
    sample.sort()   #ordena la lista de numeros de manera ascendente
    return sample  #devuelve la lista ordenada


#medir el tiempo de cada ejecucion ---  (〃￣︶￣)人(￣︶￣〃)

def medir_tiempo(func, data, x): #recibe una funcion(func), una lista(data), y el valor a buscar(x)
    t0 = time.perf_counter()  #permite medir tiempos cortos 
    index = func(data, x)
    t1 = time.perf_counter() #detiene el cronometro.... salu2
    ms = (t1 - t0) * 1000.0  #se calcula el tiempo y se convierten a milisegundos al multiplicarlos por mil  
    return index, ms

#promediar los tiempos de ejecucion para los datos de la grafica --- (ง •_•)ง

def promedio_tiempo(sizes, repeticiones=5, modo="peor_caso"):
    results = {"lineal": [], "binaria": []} #aqui se guardara el timepo promedio de cada algoritmo para cada lista

    for size in sizes: #itera sobre cada lista a evaluar
        tiempo_lineal = [] #lista donde se guardara el tiempo de ejecucion
        tiempo_binario = []

        for _ in range(repeticiones):
            data = generar_lista_ordenada(size)
            if modo == "peor_caso":  
                x = size * 10 + 1  #si no esta en la lista eligira un numero fuera del rango lo que indica que no esta 
            else: 
                x= data[-1] #si se encuentra indica el ultimo numero de la lista, esto significa que si se encuentra
            
            _, t_lin = medir_tiempo(busqueda_lineal, data, x) #mide los tiempos de la busqueda 
            _, t_bin = medir_tiempo(busqueda_binaria, data, x)

            tiempo_lineal.append(t_lin) #se alamcena el tiempo obtenido
            tiempo_binario.append(t_bin)

        results["lineal"].append(sum(tiempo_lineal) / len(tiempo_lineal))  #se calcula el tiempo promedio de los algoritmos y se guarda en results
        results["binaria"].append(sum(tiempo_binario) / len(tiempo_binario))
    return results

#Interfaz GUI  --- <(＿　＿)>

class GUI(tk.Tk):  #obtiene tk.Tk para hacer una ventana principal
    def __init__(self):
        super().__init__()
        self.title("Comparacion de busqueda Lineal y Binaria")  #titulo de la GUI
        self.geometry("980x680") #tamaño de la GUI

        self.data = None
        self.sizes_valid = [100, 1000, 10000, 100000]  #Para generar las longitudes de las listas a evaluar

        self.configure(bg="#ffdc90")
        style = ttk.Style()
        try:
            style.theme_use('clam')
        except Exception:
            pass
        style.configure("Custom.TFrame", background="#ffdc90")
        style.configure("Custom.TLabel", background="#ffdc90")
        style.configure("Custom.TButton", font=("Segoe UI", 9), padding=6)

        # Frame central que contendrá los controles centrados
        center_frame = ttk.Frame(self, padding=12, style="Custom.TFrame")
        center_frame.pack(side=tk.TOP, expand=False)

        # Usamos un frame interno para apilar los controles uno debajo del otro y centrarlos
        controls = ttk.Frame(center_frame, padding=8, style="Custom.TFrame")
        controls.pack(anchor="center")

        # Tamaño lista y generar datos
        ttk.Label(controls, text="Tamaño lista:", style="Custom.TLabel").pack(pady=4)
        self.combo_size = ttk.Combobox(controls, values=[str(s) for s in self.sizes_valid], state="readonly", width=12)
        self.combo_size.current(0)
        self.combo_size.pack(pady=2)

        self.btn_generate = ttk.Button(controls, text="Generar datos", command=self.onGenerar, style="Custom.TButton") #botton para generar los datos aleatorios
        self.btn_generate.pack(pady=6)

        self.lbl_status = ttk.Label(controls, text="Sin datos generados.", foreground="gray", style="Custom.TLabel") #muestra un mensaje que indica que no hay datos generados
        self.lbl_status.pack(pady=4)

        # Entrada de valor y botones de búsqueda
        entry_frame = ttk.Frame(center_frame, padding=6, style="Custom.TFrame")
        entry_frame.pack(anchor="center", pady=6)

        ttk.Label(entry_frame, text="Valor a buscar (entero):", style="Custom.TLabel").pack(side=tk.LEFT, padx=(0,6))   #valor a buscar
        self.entry_x = ttk.Entry(entry_frame, width=14)
        self.entry_x.pack(side=tk.LEFT, padx=(0,10))

        self.btn_lineal = ttk.Button(entry_frame, text="Busqueda lineal", command=self.onBuscarLineal, style="Custom.TButton") #boton para ejecutar la busqueda lineal
        self.btn_lineal.pack(side=tk.LEFT, padx=4)

        self.btn_binaria = ttk.Button(entry_frame, text="Busqueda binaria", command=self.onBuscarBinaria, style="Custom.TButton") #boton para ejecutar la busqueda binaria
        self.btn_binaria.pack(side=tk.LEFT, padx=4)

        # Resultados en un LabelFrame (mantengo estructura original dentro)
        res = ttk.LabelFrame(self, text="Resultados de la ultima busqueda", padding=10)  #muestra los resultados de la busqueda
        res.pack(side=tk.TOP, fill=tk.X, padx=10, pady=(5, 10))

        self.var_size = tk.StringVar(value="-")    #se almacenan los valores
        self.var_found = tk.StringVar(value="-")
        self.var_time = tk.StringVar(value="-")

        ttk.Label(res, text="Tamaño de la lista:").grid(row=0, column=0, sticky="w")   # resultado de la lista usada
        ttk.Label(res, textvariable=self.var_size).grid(row=0, column=1, sticky="w")

        ttk.Label(res, text="Resultado:").grid(row=1, column=0, sticky="w")  #restulado del valor
        ttk.Label(res, textvariable=self.var_found).grid(row=1, column=1, sticky="w")

        ttk.Label(res, text="Tiempo de ejecucion (ms):").grid(row=2, column=0, sticky="w") #resultado del tiempo de ejecucion
        ttk.Label(res, textvariable=self.var_time).grid(row=2, column=1, sticky="w")

    
        graf_ctrl = ttk.Frame(self, padding=10)   #apartado que permite la creacion de la grafica
        graf_ctrl.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(graf_ctrl, text="Repeticiones(minimo 5):").grid(row=0, column=0, sticky="w") 
        self.spin_reps = tk.Spinbox(graf_ctrl, from_=1, to=100, width=5)
        self.spin_reps.delete(0, tk.END)
        self.spin_reps.insert(0, "5")
        self.spin_reps.grid(row=0, column=1, padx=5)

        ttk.Label(graf_ctrl, text="Modo:").grid(row=0, column=2, sticky="w", padx=(15, 0))
        self.combo_mode = ttk.Combobox(graf_ctrl, values=["peor_caso", "ultimo"], state="readonly", width=12)
        self.combo_mode.current(0)
        self.combo_mode.grid(row=0, column=3, padx=5)

        self.btn_plot = ttk.Button(graf_ctrl, text="Actualizar", command=self.onActualizarGrafica)
        self.btn_plot.grid(row=0, column=4, padx=10)

      
        graf_frame = ttk.LabelFrame(self, text="Comparacion de tiempos promedio", padding=10)  #compara los tiempos
        graf_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        self.fig = Figure(figsize=(7.8, 4.2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("Tamaño de la lista")
        self.ax.set_ylabel("Tiempo promedio (ms)")
        self.ax.set_title("Lineal vs Binaria (promedios)")

        self.canvas = FigureCanvasTkAgg(self.fig, master=graf_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        
        self.dibujar_grafica_vacia()   #muestra la grafica, de momento vacia hasta ue no se generen datos

    def onGenerar(self):  
        size_str = self.combo_size.get().strip()  #toma el valor seleccionado 
        if not size_str.isdigit():
            messagebox.showerror("Error", "Selecciona un tamaño valido.")  
            return
        size = int(size_str)
        if size not in self.sizes_valid:  #revisa que sea un valor valido
            messagebox.showerror("Error", "El tamaño debe ser uno de: 100, 1000, 10000, 100000.")  
            return
        
        self.data = generar_lista_ordenada(size) #llama a la funcion para generar una lista 
        self.lbl_status.configure(text=f"Elementos generados: {size}", foreground="blue") 
        self.var_size.set(f"{size:,}".replace(","," "))
        self.var_found.set("-")
        self.var_time.set("-")

    def onBuscarLineal(self):
        self._buscar_con_algoritmo(busqueda_lineal, "lineal") #se pasa a buscar con algoritmo con la funcion necesaria lineal o binaria

    def onBuscarBinaria(self):
        self._buscar_con_algoritmo(busqueda_binaria, "binaria")

    def _buscar_con_algoritmo(self, algoritmo, name):
        if self.data is None:
            messagebox.showwarning("Atencion", "Primero genera los datos.") #valida que se generen los datos
            return
        
        x_str = self.entry_x.get().strip()  #verifica que se haya ingresado un nuvero valirdo
        if x_str == "":
            messagebox.showerror("Error", "Ingresa un valor entero") #que se ingrese un valor permitido
            return
        if not x_str.lstrip("-").isdigit():
            messagebox.showerror("Error", "El valor a buscar debe ser un entero positivo o negativo")
            return
        
        x = int(x_str)
        index, ms = medir_tiempo(algoritmo, self.data, x)  #llama a la funcion para medir el tiempo

        self.var_size.set(f"{len(self.data):,}".replace(",", " "))
        if index == -1:
            self.var_found.set("no encontrado")
        else:
            self.var_found.set(str(index))
        self.var_time.set(f"{ms:.3f}")

#actualiza la grafica --- (⓿_⓿)

    def onActualizarGrafica(self):
        reps_str = self.spin_reps.get().strip()
        if not reps_str.isdigit(): 
            messagebox.showerror("Error", "Las repeticiones deben ser un valor entero")  
            return
        repeticiones = int(reps_str)
        if repeticiones < 5:  #valida que sean minimo 5 repeticiones
            messagebox.showerror("Error", "Como minimo deben ser 5 repeticiones")
            return
        
        mode = self.combo_mode.get()
        self.btn_plot.config(state=tk.DISABLED) #cambia el estado del boton a desactivado para evitar varias ejecuciones del mismo mientras se calcula
        self.btn_plot.update_idletasks()

        sizes = self.sizes_valid[:]
        results = promedio_tiempo(sizes, repeticiones=repeticiones, modo=mode)  #obtene los promedios de los tiempos mediante la funcion para calcularlos

        self.btn_plot.config(state=tk.NORMAL)
        self.dibujar_barras(sizes, results["lineal"], results["binaria"])  #dibuja una nueva grafica en base a los resultados

#dibujar la grafica con las barras --- ( •̀ ω •́ )✧

    def dibujar_grafica_vacia(self):
        self.ax.clear()  #elimina cualquier valor anterior de la grafica
        self.ax.set_xlabel("Tamaño de lista")     
        self.ax.set_ylabel("Tiempo promedio (ms)")
        self.ax.set_title("Promedios")
        self.ax.set_xticks(range(len(self.sizes_valid))) #utiliza el tamaño de lista seleccionado
        self.ax.set_xticklabels([f"{s:,}".replace(",", " ") for s in self.sizes_valid])
        self.ax.grid(True, axis="y", linestyle="--", alpha=0.4)
        self.canvas.draw()

    def dibujar_barras(self, sizes, times_lineal, times_binario):
            self.ax.clear()  #limpia el grafico
            labels = [f"{s:,}".replace(",", " ") for s in sizes]

            x = np.arange(len(sizes))  #calcula las posiciones en x 
            width = 0.35

            self.ax.bar(x - width/2, times_lineal, width=width, label="Lineal", color="#007DA3")   #dibuja dos barras 
            self.ax.bar(x + width/2, times_binario, width=width, label="Binaria", color="#059E0A")

            self.ax.set_xticks(x) #define donde se ubicaran las etiquetas 
            self.ax.set_xticklabels(labels)  #textos que se mostraran abajo de las barras
            self.ax.set_xlabel("Tamaño de la lista")
            self.ax.set_ylabel("Tiempo promedio en ms")
            self.ax.set_title("Comparacion de tiempos") #promedio de las repeticiones seleccionadas 
            self.ax.grid(True, axis="y", linestyle="--", alpha=0.4) 
            self.ax.legend() #muestra los colores correspondientes a cada barra

            for i in range(len(sizes)): #recorre todas las posiciones de las barras
                self.ax.text(x[i] - width/2, times_lineal[i], f"{times_lineal[i]:.2f}", ha="center", va="bottom", fontsize=8) #valores de estilo de la barra lineal
                self.ax.text(x[i] + width/2, times_binario[i], f"{times_binario[i]:.2f}", ha="center", va="bottom", fontsize=8) #valores de estilo de la barra binaria

            self.canvas.draw() #redibuja la grafica

if __name__ == "__main__":
    random.seed(42)  #para que los valores random sean reproducibles
    gui = GUI()  #crea una instancia de la GUI
    gui.mainloop()
