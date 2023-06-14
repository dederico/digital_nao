Movie Ratings App
================

The Movie Ratings App is a web application that allows users to search for movie titles and retrieve their ratings using the TMDb API (The Movie Database). It provides a simple interface where users can enter a movie title, and the application fetches the rating for the first matching result.

Prerequisites
-------------
- Python 3.7 or higher
- Flask web framework
- requests library
- python-dotenv library

Getting Started
---------------
1. Clone the repository

2. Install the required dependencies using pip:

pip install -r requirements.txt

3. Obtain a TMDb API key:
- Visit the TMDb website: https://www.themoviedb.org/
- Sign up for an account and obtain an API key.
- Replace the value of the `API_KEY` variable in the `.env` file with your API key.

4. Run the application:


5. Access the application:
Open your web browser and visit `http://localhost:5000` to access the Movie Ratings App.

Usage
-----
- Enter a movie title in the input field and click the "Buscar" (Search) button.
- The application will retrieve the rating for the first matching result and display it on the page.
- If no rating is found or if an error occurs, an appropriate message will be displayed.

Contributing
------------
Contributions to the Movie Ratings App are welcome! If you find any issues or would like to add new features, please open an issue or submit a pull request.

License
-------
This project is licensed under the [MIT License](LICENSE).

Contact
-------
For any questions or inquiries, please contact me at dederico@gmail.com
