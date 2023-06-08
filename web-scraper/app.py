from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Realizar la solicitud a la página web
    url = 'https://www.facebook.com'
    response = requests.get(url)
    
    # Extraer los datos utilizando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ejemplo de extracción de título de la página
    title = soup.find('title')
    
    # Ejemplo de extracción de texto de un elemento específico
    content = soup.find('div', class_='home-container')
    
    # Ejemplo de extracción de imágenes
    images = []
    image_elements = soup.find_all('img', class_='product-card-image')
    for image_element in image_elements:
        image_url = image_element['src']
        images.append(image_url)
    
    # Ejemplo de extracción de enlaces
    links = []
    link_elements = soup.find_all('a')
    for link_element in link_elements:
        if 'href' in link_element.attrs:
            link_url = link_element['href']
            links.append(link_url)
    
    # Renderizar la plantilla HTML y pasar los datos al contexto
    return render_template('index.html', title=title, content=content, images=images, links=links)

if __name__ == '__main__':
    app.run()
