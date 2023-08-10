 
import datetime
import pprint
import pymongo 

# É necessário instalar o pymongo[srv], um Servidor DNS nativo do python utilizado na conexão com MongoDB

string_connection = "mongodb+srv://luizfarias:<password>@cluster0.3cjqmen.mongodb.net/?retryWrites=true&w=majority"

# Conectando ao Mongo DB
client = pymongo.MongoClient(string_connection)

db = client.test

# Cirando uma Collection

collection = db.test_collection

# Criando Documentos

post =[ {{
        "id":1,
        "nome":"Luiz Henrique",
        "cpf": 12345678910,
        "endereco": "Av Santa Fe, numero 675, Francisco Beltrão - SP",
        "conta":{
            "id": 23,
            "tipo": "Corrente",
            "agencia": "0001",
            "num_conta": 2390,
            "Id_cliente": 1,
            "Saldo": 23
            }
    },{
        "id":2,
        "nome":"Ana Fagundes",
        "cpf": 89076533210,
        "endereco": "Rua Paulo Abreu, numero 900, Terra Da Uva Jundiaí - SP",
        "conta":{
            "id": 23,
            "tipo": "Poupança",
            "agencia": "0001",
            "num_conta": 2392,
            "Id_cliente": 2,
            "Saldo": 900
        } 
    }
}]

posts = db.posts

results = posts.insert_many(post)

print(results.inserted_ids)