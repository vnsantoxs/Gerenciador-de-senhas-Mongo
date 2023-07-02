from pymongo import MongoClient

def create_app(nome_aplicativo, senha):
    client = MongoClient('localhost', 27017)
    db = client['gerenciador_de_senhas']
    collection = db['gerenciamento']
    aplicativo = {
        'nome_aplicativo': nome_aplicativo,
        'senha': senha
    }
    result = collection.insert_one(aplicativo)
    print('Aplicativo criado com o ID:', result.inserted_id)
    client.close()

def list_apps():
    client = MongoClient('localhost', 27017)
    db = client['gerenciador_de_senhas']
    collection = db['gerenciamento']
    aplicativos = collection.find()
    return list(aplicativos)

def update_app(nome_aplicativo, nova_senha):
    client = MongoClient('localhost', 27017)
    db = client['gerenciador_de_senhas']
    collection = db['gerenciamento']
    query = {'nome_aplicativo': nome_aplicativo}
    new_values = {'$set': {'senha': nova_senha}}
    result = collection.update_one(query, new_values)
    print(result.modified_count, 'documento atualizado')
    client.close()

def delete_app(nome_aplicativo):
    client = MongoClient('localhost', 27017)
    db = client['gerenciador_de_senhas']
    collection = db['gerenciamento']
    query = {'nome_aplicativo': nome_aplicativo}
    result = collection.delete_one(query)
    print(result.deleted_count, 'documento excluído')
    client.close()

def search_app(nome_aplicativo):
    client = MongoClient('localhost', 27017)
    db = client['gerenciador_de_senhas']
    collection = db['gerenciamento']
    query = {'nome_aplicativo': nome_aplicativo}
    aplicativo = collection.find_one(query)
    print(aplicativo)
    return aplicativo


