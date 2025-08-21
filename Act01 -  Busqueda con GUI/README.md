# ReadMe de Act01 - Búsqueda con GUI

El código presenta una interfaz de usuario que permite crear una lista de números aleatorios y posteriormente buscar un número mediante dos métodos: **búsqueda lineal** y **búsqueda binaria**. La lista puede generarse en cuatro tamaños distintos: 100, 1000, 10000 y 100000. Una vez seleccionada y generada la lista, en el recuadro correspondiente se ingresa un número entero para realizar la búsqueda, eligiendo entre los dos métodos disponibles. Al finalizar, si el número se encuentra, el programa muestra el índice en el que aparece; en caso contrario, indica que no se encontró, mostrando además el tiempo de ejecución en ambos casos. Las pruebas se realizan con un mínimo de cinco repeticiones para obtener resultados más consistentes, y al dar clic en el botón **Actualizar** se despliega una gráfica con los promedios de los tiempos de ejecución.

## Requisitos
- **Python 3.13.2** o superior

## Librerías externas usadas
- **numpy**: librería para cálculos numéricos, utilizada en la generación de datos y las barras de la gráfica.  
- **matplotlib**: librería para la creación de gráficas, en este caso integrada dentro de la misma ventana de la GUI.  

