from flask import Flask
from flask import request
from flask import render_template 

app = Flask(__name__) #Nuevo objeto,

@app.route('/') #wrap o un decorador 
def index():   #funcion que regrsa un string
    title = "Curso Flask"
    return render_template('index.html',title=title)


if __name__ == '__main__':
    app.run( debug =True, port=8000)  #se encarga de ejecutar el servidor en el puerto 5000