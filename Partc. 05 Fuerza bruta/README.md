# ReadMe de Partc. 05 - Fuerza Bruta

El código presenta una interfaz de usuario que permite ingresar cinco puntos en un plano cartesiano y calcular las distancias entre cada par de puntos usando el método de **fuerza bruta**. Los puntos pueden ingresarse de manera manual o generarse aleatoriamente. La aplicación muestra paso a paso los cálculos de la distancia usando la fórmula de distancia euclidiana y destaca la **distancia mínima** y **distancia máxima** entre los puntos ingresados.

## Funcionamiento
- **Llenar**: genera cinco puntos aleatorios y los muestra en las entradas de la GUI.  
- **Calcular**: calcula todas las distancias entre los puntos y las muestra en la ventana de resultados.  
- **Limpiar**: borra los puntos ingresados y los resultados de la ventana de texto.  
- La aplicación también incluye un **modo consola** que permite ejecutar las mismas funciones desde la terminal de Python.

## Requisitos
- **Python 3.x**

## Librerías externas usadas
- **Tkinter**: librería estándar de Python para la creación de interfaces gráficas.  
- **math**: librería estándar de Python para cálculos matemáticos, utilizada para calcular la distancia euclidiana entre los puntos.  
- **random**: librería estándar de Python para generar números aleatorios, usada para crear puntos aleatorios.  
- **threading**: librería estándar de Python para manejar la ejecución simultánea del bucle de consola sin bloquear la GUI.
