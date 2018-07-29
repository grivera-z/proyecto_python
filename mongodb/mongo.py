from flask import Flask
from flask import request
from flask import render_template 
from flask_pymongo import PyMongo


app = Flask(__name__) #Nuevo objeto,
app.config["MONGO_URI"] = "mongodb://localhost:27017/curso_mean2"
mongo = PyMongo(app)

@app.route("/")
@app.route("/<Documents>")
def home_page(Documents='albums'):
    Results = mongo.db["artists"].find()
    array = list(Results)
    Coll_Names = mongo.db.collection_names()
    # Coll_list = []
    # for i in Coll_Names:
    #     Coll_list.append('<option value="'+ i+'">'+i+'</option>')
    return render_template("index.html",Results=array,Title=Documents.upper(),Coll_Names=Coll_Names)

# @app.route('/') #wrap o un decorador 
# def index():   #funcion que regrsa un string
#     title = "Curso Flask"
#     return render_template('index.html',title=title)


if __name__ == '__main__':
    app.run( debug =True, port=8000)  #se encarga de ejecutar el servidor en el puerto 5000