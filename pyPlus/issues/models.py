import json

from ..core import r
from ..helpers import JsonSerializer, DriveServices


class ProductJsonSerializer(JsonSerializer):
    pass


class Issue(ProductJsonSerializer):

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

        t = Issue()

        t.name = name
        t.description = description
        t.order = order

        print "Entramos a new "
        print name
        print t
        return t


    def save(self):
        print "Entramos a Issue model save"
        driveServices = DriveServices()
        folde = driveServices.create_folder( self.name, self.description, "root")
        self.id = folde['id'].encode('utf8')
        r.hset("issue", self.id, json.dumps(self.to_json()))

    @classmethod
    def all(self):
        lista = r.hgetall("issue")
        l = []
        for issue in lista:
            i = json.loads( lista[issue])
            l.append( i )

        return l

    @classmethod
    def get(self , id):

        issue = json.loads(r.hget("issue",id))
        t = Issue()
        t.id = issue['id'].encode('utf8')
        t.description = issue['description'].encode('utf8')
        t.name = issue['name'].encode('utf8')
        t.order = issue['order'].encode('utf8')


        return t


    def update(self ):


        driveServices = DriveServices()

        driveServices.update_folder(self.id, self.name, self.description)
        r.hset("issue", self.id, json.dumps(self.to_json()))

        return self


    def delete(self , id=None):
        driveServices = DriveServices()

        if id != None:
            self.id = id

        if self.id != None:
            driveServices.delete_file(self.id)
            r.hdel("issue" ,self.id )
            return True

        return False

