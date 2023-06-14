from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        ussd_text = request.form.get('text', '')
        response = process_option(ussd_text)
        return response

    return render_template('index.html')

def process_option(option):
    if option == '1':
        return 'Su saldo actual es: $100'
    elif option == '2':
        return 'Recarga exitosa. Nuevo saldo: $200'
    elif option == '3':
        return 'Transferencia realizada correctamente'
    elif option == '4':
        return '¡Hasta luego! Gracias por usar nuestro menú telefónico USSD.'
    else:
        return 'Opción inválida. Por favor, seleccione una opción válida.'

if __name__ == '__main__':
    app.run()
