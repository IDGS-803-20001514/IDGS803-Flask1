from flask import Flask, render_template
from flask import request  #Para las peticiones HTTP

app = Flask(__name__)

@app.route('/HolaMundo')
def index():
    return '!!!!Hello World¡¡¡¡ otra cosa'

################# TEMA 2 #####################

@app.route("/hola")
def hola():
    return "<h1> Saludo desde Hola </h1>"

@app.route("/nueva")
def nueva():
    return "<h1> Saludo desde Nueva </h1>"


#############################################

@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user + " desde la URL user"


################# TEMA 3 #####################

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}  es un entero.".format(n)

@app.route("/infoUser/<int:n>/<string:nombre>")
def infoUser(n, nombre):
    return "Hola {} tu edad es {}".format(nombre, n)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1+n2)

################# TEMA 4 #####################

@app.route("/operacionesBasicas", methods=['GET','POST'])
def operacionesBasicas():
    
    if request.method == 'POST':
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")

        return "El resultado es: {}".format(str(int(num1)+int(num2)))
    else:
        
        return '''
            <form action="/operacionesBasicas" method="POST">
            <label for="num1">Numero 1:</label>
            <input type="text" name="num1"><br>
            <label for="num2">Numero 2:</label>
            <input type="text" name="num2"><br>
            <input type="submit" value="Enviar">
            </form>
        '''
    
################# TEMA 5 #####################

@app.route("/", methods=['GET','POST'])
def indexRenderTemplate():
    nombre = "Filemona"
    lista = ["Español", "Ingles", "Quimica"]
    return render_template("index.html", nombre=nombre, lista=lista)

@app.route("/usuarios", methods=['GET','POST'])
def archivo2Template():
    return render_template("archivo2.html")

if __name__ == '__main__':
    app.run(debug=True)