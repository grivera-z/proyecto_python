from flask import Flask
from flask import request 

app = Flask(__name__) #Nuevo objeto,

@app.route('/') #wrap o un decorador 
def index():   #funcion que regrsa un string
    return 'Hola Mundo que hola'

@app.route('/params') #wrap o un decorador 
def params():   #funcion que regrsa un string
    param = request.args.get('params1','no contiene nada')
    return 'otro mensaje {}'.format(param)

if __name__ == '__main__':
    app.run( debug =True, port=8000)  #se encarga de ejecutar el servidor en el puerto 5000