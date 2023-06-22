# Paint App

Esta es una aplicación simple de pintura en pantalla que te permite dibujar utilizando el cursor del mouse. Puedes seleccionar diferentes colores y pintar en un lienzo virtual.

## Tecnologías utilizadas

- Python 3.9+: Lenguaje de programación utilizado para el desarrollo de la aplicación.
- Tkinter: Librería gráfica de Python para crear interfaces de usuario.
- Tkinter ttk: Módulo adicional de Tkinter que proporciona estilos mejorados para los widgets.

## Instalación

1. Asegúrate de tener instalada la versión adecuada de Python en tu sistema. Puedes descargar Python desde el sitio web oficial: https://www.python.org/downloads/

2. Clona o descarga el repositorio de GitHub en tu máquina local.

   $ git clone https://github.com/tu-usuario/paint-app.git

3. Accede al directorio del proyecto.

   $ cd paint-app

4. Opcionalmente, crea y activa un entorno virtual para mantener las dependencias del proyecto aisladas.

   $ python -m venv venv
   $ source venv/bin/activate  # En sistemas UNIX
   $ venv\Scripts\activate  # En sistemas Windows

5. Instala las dependencias del proyecto utilizando pip, el gestor de paquetes de Python.

   $ pip install -r requirements.txt

## Ejecución

1. Desde el directorio del proyecto, ejecuta el archivo main.py con Python.

   $ python main.py

2. La aplicación se abrirá en una nueva ventana.

3. Utiliza el cursor del mouse para dibujar en el lienzo.

4. Selecciona los colores disponibles haciendo clic en los botones correspondientes.

5. Para borrar todo el dibujo, haz clic en el botón "Clear".

6. Cierra la aplicación cuando hayas terminado de usarla.

## Cómo funciona

La aplicación utiliza la biblioteca Tkinter de Python para crear una interfaz gráfica de usuario (GUI). Los eventos del mouse se capturan utilizando los métodos bind() para detectar cuándo se presiona, se mueve o se suelta el botón del mouse.

Cuando el botón del mouse se presiona y se mueve (<B1-Motion>), se dibujan pequeños óvalos en el lienzo en las coordenadas correspondientes. El color del óvalo se determina según el color seleccionado en ese momento.

Para cambiar el color, puedes hacer clic en los botones de colores disponibles. Al hacer clic en el botón "Clear", se borra todo el contenido del lienzo.

## Contribución

Si deseas contribuir a este proyecto, puedes seguir los siguientes pasos:

1. Realiza un fork del repositorio en GitHub.

2. Clona tu repositorio fork en tu máquina local.

   $ git clone https://github.com/tu-usuario/paint-app.git

3. Crea una rama para tus cambios.

   $ git checkout -b feature/nueva-funcionalidad

4. Realiza los cambios y realiza los commits correspondientes.

   $ git commit -m "Agrega nueva funcionalidad"

5. Envía tus cambios al repositorio fork.

   $ git push origin feature/nueva-funcionalidad

6. Abre un pull request en el repositorio original para revisar tus cambios.
