import pymongo
import json

uri = "mongodb+srv://allAccess:P8OxiNrhuJ4YH3bI@projcluster.zt93x.mongodb.net/?retryWrites=true&w=majority&appName=ProjCluster"
client = pymongo.MongoClient(uri)

db = client["Projeto"]  

colecao = db["Aluno"]  

with open('jsons\insertAlunos.json', 'r') as f:
    dados = json.load(f)

if isinstance(dados, list):
    colecao.insert_many(dados)
else:
    colecao.insert_one(dados)
    

colecao = db["Professor"]  

with open('jsons\insertProfs.json', 'r') as f:
    dados = json.load(f)

if isinstance(dados, list):
    colecao.insert_many(dados)
else:
    colecao.insert_one(dados)
    
colecao = db["Matriz"]  

with open('jsons\insertMatriz.json', 'r') as f:
    dados = json.load(f)

if isinstance(dados, list):
    colecao.insert_many(dados)
else:
    colecao.insert_one(dados)
    
print("Coleções criadas e dados inseridos")

