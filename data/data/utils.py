from pymongo import MongoClient

def get_client(uri):
    return MongoClient(uri)

def get_DB(client,DBname):
    return client[DBname]

def get_col(DB,colname):
    return DB[colname]

def get_doc(col,query):
    return col.find_one(query,{'_id':0})

def get_DB_dir(uri,DBname):
    return MongoClient(uri)[DBname]

def get_col_dir(uri,DBname,colname):
    return MongoClient(uri)[DBname][colname]

def get_doc_dir(uri,DBname,colname,query):
    return MongoClient(uri)[DBname][colname].find_one(query,{'_id':0,'title':0})

def update_doc(col,update,docquery):
    col.update_one(docquery,update)

