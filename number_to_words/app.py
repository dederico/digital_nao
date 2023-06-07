from flask import Flask, render_template, request

app = Flask(__name__)

def number_to_words(number):
    units = [
        "cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
        "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
        "dieciocho", "diecinueve"
    ]
    tens = [
        "", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"
    ]
    if number < 20:
        return units[number]
    elif number < 100:
        if number % 10 == 0:
            return tens[number // 10]
        else:
            return tens[number // 10] + " y " + units[number % 10]
    else:
        return "Número fuera de rango"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = int(request.form['number'])
        if number < 0 or number > 99:
            result = "Número fuera de rango"
        else:
            result = number_to_words(number)
        return render_template('index.html', result=result)
    else:
        return render_template('index.html', result='')

if __name__ == '__main__':
    app.run()
