Hangman Game

Este es un juego del ahorcado implementado en Python utilizando la biblioteca Tkinter para la interfaz gráfica.

Descripción del juego:
El juego selecciona aleatoriamente una palabra de una lista predefinida. El jugador debe adivinar la palabra ingresando letras en una interfaz gráfica. Si la letra adivinada está en la palabra, se muestra en su posición correspondiente en la palabra oculta. Si la letra no está en la palabra, se muestra un contador de intentos restantes y se dibuja el ahorcado gradualmente en la interfaz gráfica.

Funcionalidades principales:
- Selección aleatoria de palabras de una lista predefinida.
- Manejo de letras adivinadas y conteo de intentos restantes.
- Actualización dinámica de la palabra oculta en la interfaz gráfica.
- Finalización del juego cuando se adivina la palabra completa o se agotan los intentos.

Ejecución del juego:
Para ejecutar el juego, se requiere tener instalado Python y la biblioteca Tkinter. Simplemente ejecuta el archivo en un intérprete de Python.

Requisitos del sistema:
- Python 3.x
- Biblioteca Tkinter

Estructura del código:
El código está dividido en diferentes funciones y utiliza la biblioteca Tkinter para crear la interfaz gráfica. Aquí están las principales funciones y componentes del código:
- `initialize_game()`: Inicializa el juego generando una palabra aleatoria y estableciendo los valores iniciales para las letras adivinadas y los intentos restantes.
- `guess_letter()`: Maneja la lógica de adivinar una letra ingresada por el jugador. Actualiza las letras adivinadas, verifica si la letra está en la palabra y muestra mensajes apropiados en la interfaz gráfica.
- `update_word_label()`: Actualiza la etiqueta de la palabra oculta en la interfaz gráfica.
- `disable_input()`: Deshabilita la entrada de texto y el botón de adivinanza cuando el juego ha terminado.
- `draw_hangman()`: Esta función se puede implementar para dibujar el ahorcado gradualmente en la interfaz gráfica, utilizando la cantidad de intentos incorrectos como base.

¡Diviértete jugando al ahorcado!

