import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_title = request.form.get('movie_title')
        if movie_title:
            api_key = ''
            url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'results' in data and data['results']:
                    movie = data['results'][0]
                    movie_id = movie['id']
                    rating_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits'
                    rating_response = requests.get(rating_url)
                    if rating_response.status_code == 200:
                        rating_data = rating_response.json()
                        if 'vote_average' in rating_data:
                            rating = rating_data['vote_average']
                            return render_template('index.html', rating=rating)
        return render_template('index.html', error=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
