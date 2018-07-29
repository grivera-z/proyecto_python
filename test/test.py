from flask import Flask
from flask import request
from flask import render_template 
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask(__name__) #Nuevo objeto,
app.config["MONGO_URI"] = "mongodb://localhost:27017/curso_mean2"
mongo = PyMongo(app)
# Results = mongo.db["artists"].find()
# array = list(Results)
# print(array)

Coll_Names = mongo.db.collection_names()
Coll_list = []
for i in Coll_Names:
    Coll_list.append('<option value="'+ i+'">'+i+'</option>')
print(Coll_list)





























# # f= open("test.txt","w+")
# # for i in range(10):
# #      f.write("This is line %d\r\n" % (i+1))
# # f.close() 

# # aux = "holaZEO"

# # s = "This be a string"
# # if aux.upper().find("ZEO") == -1:
# #     print("No 'is' here!")
# # else:
# #     print ("Found 'is' in the string.")
# import json
# alist = [{
#     "_id": "5b56a99bf7b348f6491fcd09",
#     "index": 0,
#     "guid": "0fb565ea-f8a4-4674-9975-50b7caae0c7c",
#     "isActive": False,
#     "balance": "$3,881.24",
#     "picture": "http://placehold.it/32x32",
#     "age": 40,
#     "eyeColor": "blue",
#     "name": "Dale Walter",
#     "gender": "female",
#     "company": "LUXURIA",
#     "email": "dalewalter@luxuria.com",
#     "phone": "+1 (930) 577-3492",
#     "address": "778 Stoddard Place, Waterford, Georgia, 9835",
#     "about": "Mollit dolor sunt do laboris excepteur fugiat excepteur duis culpa. Proident sint ipsum laboris enim. Do cupidatat sint consequat non id eiusmod ipsum eu amet. Eiusmod occaecat aliquip ut aliquip ea consectetur velit. Irure adipisicing ullamco et ipsum dolor. Amet officia in aliquip id in Lorem adipisicing.\r\n",
#     "registered": "2016-12-27T07:23:22 +06:00",
#     "latitude": -6.311751,
#     "longitude": 29.221591
# },{
#     "_id": "5b56a99bf7b348f6491fcd09",
#     "index": 0,
#     "guid": "0fb565ea-f8a4-4674-9975-50b7caae0c7c",
#     "isActive": False,
#     "balance": "$3,881.24",
#     "picture": "http://placehold.it/32x32",
#     "age": 40,
#     "eyeColor": "blue",
#     "name": "Dale Walter",
#     "gender": "female",
#     "company": "LUXURIA",
#     "email": "dalewalter@luxuria.com",
#     "phone": "+1 (930) 577-3492",
#     "address": "778 Stoddard Place, Waterford, Georgia, 9835",
#     "about": "Mollit dolor sunt do laboris excepteur fugiat excepteur duis culpa. Proident sint ipsum laboris enim. Do cupidatat sint consequat non id eiusmod ipsum eu amet. Eiusmod occaecat aliquip ut aliquip ea consectetur velit. Irure adipisicing ullamco et ipsum dolor. Amet officia in aliquip id in Lorem adipisicing.\r\n",
#     "registered": "2016-12-27T07:23:22 +06:00",
#     "latitude": -6.311751,
#     "longitude": 29.221591
# }]


# sorted_list = sorted(alist[0].items(), key = lambda x:x[0])
# print(dict(sorted_list))
# print(type(sorted_list[0]))



















