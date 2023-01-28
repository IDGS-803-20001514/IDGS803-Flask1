from flask import Flask
from flask import request  #Para las peticiones HTTP

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")

        operacion = request.form.get("operacion")

        if operacion == 'suma':
            return "El resultado es: {}".format(str(int(num1)+int(num2)))
        elif operacion == 'resta':
            return "El resultado es: {}".format(str(int(num1)-int(num2)))
        elif operacion == 'multiplicacion':
            return "El resultado es: {}".format(str(int(num1)*int(num2)))
        else:
            return "El resultado es: {}".format(str(int(num1)/int(num2)))

    else:
        
        return '''
            <form action="/" method="POST">
            <label for="num1">Numero 1:</label>
            <input type="text" name="num1"><br>
            <label for="num2">Numero 2:</label>
            <input type="text" name="num2"><br>
            <label>Suma</label>
            <input type="radio" id="suma" name="operacion" value="suma">
            <label>Resta</label>
            <input type="radio" id="resta" name="operacion" value="resta">
            <label>Multiplicacion</label>
            <input type="radio" id="multiplicacion" name="operacion" value="multiplicacion">
            <label>Division</label>
            <input type="radio" id="division" name="operacion" value="division"><br>
            <input type="submit" value="Enviar">
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)