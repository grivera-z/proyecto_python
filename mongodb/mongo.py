from flask import Flask
from flask import request
from flask import render_template 
from flask_pymongo import PyMongo


app = Flask(__name__) #Nuevo objeto,
app.config["MONGO_URI"] = "mongodb://localhost:27017/curso_mean2"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    Results = mongo.db["artists"].find()
    array = list(Results)
    f= open("test.txt","w+")
    f.write(str(array))
    f.close() 
    return render_template("index.html",Results=array)

# @app.route('/') #wrap o un decorador 
# def index():   #funcion que regrsa un string
#     title = "Curso Flask"
#     return render_template('index.html',title=title)


if __name__ == '__main__':
    app.run( debug =True, port=8000)  #se encarga de ejecutar el servidor en el puerto 5000