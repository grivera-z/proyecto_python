from flask import Flask
from flask import request
from flask import render_template 

app = Flask(__name__) #Nuevo objeto,

@app.route('/user/<name>') #wrap o un decorador 
def user(name='Gabriel'):   #funcion que regrsa un string
    age=17
    my_list= [1,2,3,4]
    return render_template('user.html',nombre=name,age=age,list=my_list)


if __name__ == '__main__':
    app.run( debug =True, port=8000)  #se encarga de ejecutar el servidor en el puerto 5000