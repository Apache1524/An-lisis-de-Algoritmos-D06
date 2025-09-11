ReadMe de Practica 01 - Mi Primera GUI

El proyecto contiene dos programas independientes que muestran el uso básico de Tkinter en Python para crear interfaces gráficas simples.

GUI 1

El primer código genera una ventana con dos etiquetas de texto y un botón. Al hacer clic en el botón, se cambia el color de las etiquetas:

La primera etiqueta pasa a rojo.

La segunda etiqueta pasa a azul.

Este ejemplo introduce el manejo de widgets como Label y Button, así como la definición de funciones que se activan mediante eventos (en este caso, el comando del botón).

GUI 2

El segundo código crea una ventana que permite al usuario escribir su nombre en un campo de texto.

Al presionar el botón “salu2 aqui”, aparece un saludo personalizado con el nombre ingresado.

Si no se escribe nada, se muestra el texto por defecto “buscando ando”.

Un segundo botón cambia el color del texto mostrado a rojo.

Este ejemplo añade el uso de Entry para entrada de texto, y demuestra cómo se pueden actualizar dinámicamente los contenidos de las etiquetas (Label).

Requisitos

Python 3.13.2 o superior

Librerías externas usadas

tkinter: librería estándar de Python para crear interfaces gráficas.

colorama (solo en GUI 1): usada para inicializar estilos de color (aunque en este caso se aplica principalmente a consola).