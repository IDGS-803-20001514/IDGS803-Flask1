from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('cinepolis.html')

@app.route('/boletos', methods=['POST'])
def procesarBoletos():

    # Obtener los datos del formulario
    nombre = request.form['nombre']
    cantidadCompradores = int(request.form.get('cantidadCompradores'))
    tarjeta = int(request.form.get('tarjetaCine'))
    cantidadBoletos = int(request.form.get('cantidadBoletos'))

    result = "No jalo"

    cantidaCalculo = cantidadCompradores * 7

            # 14              15
    if cantidaCalculo < cantidadBoletos:
         
        result = "No puedes comprar esa cantidad de boletos {}".format(nombre)
    
    else:

        if cantidadCompradores == 1 and cantidadBoletos > 7:

            result = 'No puedes comprar mas de 7 boletos {}'.format(nombre)
        
        elif cantidadCompradores >= 1 and cantidadBoletos <= 7:
            
            if cantidadBoletos > 5 and tarjeta == 1:

                precio = cantidadBoletos * 12

                result = precio - (precio * 0.15)

                result = result - (result * 0.10)

                result = result

            elif cantidadBoletos > 5 and tarjeta == 0:

                precio = cantidadBoletos * 12

                result = precio - (precio * 0.15)

                result = result

            elif cantidadBoletos <= 5 and cantidadBoletos >= 3 and tarjeta == 1:

                precio = cantidadBoletos * 12

                result = precio - (precio * 0.10)

                result = result - (result * 0.10)

                result = result

            elif cantidadBoletos <= 5 and cantidadBoletos >= 3 and tarjeta == 0:

                precio = cantidadBoletos * 12

                result = precio - (precio * 0.10)

                result = result

            elif cantidadBoletos <= 2 and tarjeta == 1:
                    
                    precio = cantidadBoletos * 12

                    result = precio - (precio * 0.10)
        
                    result = result
                    
            elif cantidadBoletos <= 2 and tarjeta == 0:
                    
                    precio = cantidadBoletos * 12
        
                    result = precio

                    result = result

    return render_template('cinepolis.html', result=result)
        
if __name__ == '__main__':
    app.run(debug=True)