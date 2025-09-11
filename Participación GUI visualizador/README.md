ReadMe de Participación - GUI Visualizador

El programa implementa un visualizador gráfico de algoritmos de ordenamiento, mostrando paso a paso cómo se ejecutan Selection Sort y Merge Sort sobre una lista de valores aleatorios.

A través de una interfaz gráfica en Tkinter, se generan barras que representan los elementos de la lista, y se van coloreando conforme avanza el algoritmo:

Color rosa (#f1a0dd): barras en estado normal.

Color amarillo (#f3e850): barras activas o comparadas en el paso actual del algoritmo.

De esta forma, el usuario puede observar de manera visual y didáctica cómo se realizan las comparaciones, intercambios y fusiones durante el proceso de ordenamiento.

Funcionalidades principales

Generar lista: crea una nueva lista de números aleatorios dentro de un rango definido.

Ordenar con Selection Sort: ejecuta el algoritmo paso a paso, resaltando los elementos que se comparan e intercambian.

Ordenar con Merge Sort: muestra gráficamente cómo el algoritmo divide y fusiona los subarreglos hasta ordenar toda la lista.

Requisitos

Python 3.13.2 o superior

Librerías usadas

tkinter: creación de la interfaz gráfica y renderizado de las barras en Canvas.

random: generación de listas de números enteros aleatorios.

time: utilizado para inicializar la semilla de números aleatorios.