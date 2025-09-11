ReadMe de Participación - Complejidad Temporal

El programa implementa tres algoritmos de ordenamiento clásicos (Bubble Sort, Merge Sort y Quick Sort) con el objetivo de analizar y comparar su complejidad temporal.

La aplicación genera listas de números aleatorios de distintos tamaños (desde 50 hasta 1000 elementos, en incrementos de 50) y mide el tiempo que tarda cada algoritmo en ordenarlas. Los resultados se muestran en una gráfica interactiva, integrada en una interfaz gráfica creada con Tkinter.

En la gráfica, cada algoritmo se representa con un color distinto:

Bubble Sort → Naranja

Merge Sort → Azul

Quick Sort → Verde oscuro

De esta manera, se puede observar cómo el tiempo de ejecución crece conforme aumenta el tamaño de la lista, lo que permite comparar de manera visual el rendimiento de cada algoritmo.

Requisitos

Python 3.13.2 o superior

Librerías externas usadas

tkinter: librería estándar de Python para la creación de interfaces gráficas.

random: usada para generar listas de números enteros aleatorios.

time: utilizada para medir con precisión el tiempo de ejecución de cada algoritmo.

matplotlib: librería de visualización, empleada para graficar los resultados.

matplotlib.backends.backend_tkagg: integra las gráficas de Matplotlib dentro de la ventana de Tkinter.