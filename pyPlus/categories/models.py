import json

from ..core import r
from ..helpers import JsonSerializer, DriveServices


class CategoryJsonSerializer(JsonSerializer):
    pass


class Category(CategoryJsonSerializer):

    id = None
    name = None
    description = None
    order = None

    def __init__(self , id = None , name = None , description = None , order = None):
        self.id = id
        self.name = name
        self.description = description
        self.order = order

    @classmethod
    def new(self , name = None , description = None , order = None):

        t = Category()

        t.name = name
        t.description = description
        t.order = order

        return t


    def save(self):
        
        lista = r.hgetall("category")
        self.id = len(lista) + 1
         
        r.hset("category", self.id, json.dumps(self.to_json()))

    @classmethod
    def all(self):
        lista = r.hgetall("category")
        l = []
        for issue in lista:
            i = json.loads( lista[issue])
            l.append( i )

        return l

    @classmethod
    def get(self , id):

        issue = json.loads(r.hget("category",id))
        t = Category()
        t.id = issue['id']
        t.description = issue['description'].encode('utf8')
        t.name = issue['name'].encode('utf8')
        t.order = issue['order'].encode('utf8')
        

        return t


    def update(self ):
        r.hset("category", self.id, json.dumps(self.to_json()))

        return self


    def delete(self , id=None):


        if id != None:
            self.id = id

        if self.id != None:

            r.hdel("category" ,self.id )
            return True

        return False

