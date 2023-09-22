from app_base.config.mysqlconnection import *

class Ciudad:
    db_name="world"

    def __init__(self,data):
        self.id=data['ID']
        self.name=data['Name']
        self.population=data['Population']

    def __str__(self):
        return  f"{self.name}"

    @classmethod
    def get_all(cls):
        sql="select * from city"
        resultado = connectToMySQL(cls.db_name).query_db(sql)
        lista_ciudades=[]
        for ciudad in resultado:
            lista_ciudades.append(cls(ciudad))
        return lista_ciudades
    


