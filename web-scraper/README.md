
**Instructivo de uso - Proyecto de Web Scraping**

1. **Requisitos previos:**
   - Python 3.x instalado en tu sistema.
   - Conexión a Internet para realizar el scraping de la página web.
   - Conocimientos básicos de Python y el uso de la terminal.

2. **Clonar el repositorio:**
   - Clona el repositorio del proyecto desde GitHub a tu máquina local.

3. **Instalar las dependencias:**
   - Abre la terminal y navega hasta el directorio del proyecto.
   - Crea y activa un entorno virtual (opcional, pero se recomienda).
   - Ejecuta el siguiente comando para instalar las dependencias:

     ```
     pip install -r requirements.txt
     ```

   - Esto instalará las bibliotecas requeridas, incluyendo `Flask` y `BeautifulSoup`.

4. **Ejecutar la aplicación:**
   - En la terminal, asegúrate de estar en el directorio del proyecto.
   - Ejecuta el siguiente comando para iniciar la aplicación:

     ```
     python app.py
     ```

   - La aplicación Flask se ejecutará en `http://127.0.0.1:5000`.
   - Abre tu navegador web e ingresa la dirección `http://127.0.0.1:5000`.
   - La página mostrará el título y el contenido extraído del sitio web.

5. **Explorar y personalizar el proyecto:**
   - Abre el archivo `app.py` en un editor de texto.
   - Dentro de la función `index`, puedes modificar la lógica de web scraping para extraer otros elementos o información del sitio web.
   - El archivo `index.html` en la carpeta `templates` define la estructura HTML de la página que muestra los resultados del web scraping. Puedes personalizar este archivo según tus necesidades.

6. **Detener la aplicación:**
   - Para detener la aplicación Flask, regresa a la terminal y presiona `Ctrl+C`.

¡Eso es todo! Ahora puedes utilizar este proyecto de web scraping como punto de partida y personalizarlo según tus requerimientos. Recuerda que el scraping de sitios web debe hacerse de manera ética y cumpliendo las políticas de uso del sitio web objetivo.
