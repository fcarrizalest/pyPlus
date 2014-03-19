import json

from ..core import r
from ..helpers import JsonSerializer, DriveServices


class ObjectJsonSerializer(JsonSerializer):
    pass


class Objects(ObjectJsonSerializer):

    id = None
    name = None
    type = None
    description = None
    issue = None
    category = None
    elemets = None
    path = None
    status = None
    

    def __init__(self , id = None , name = None , type = None, 
                 description = None, issue =None , category = None, 
                 elements = None , path = None , status = None ):
        
        
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.issue = issue
        self.category = category
        self.elemets = elements
        self.path = path
        self.status = status

    @classmethod
    def new(self , id = None , name = None , type = None, 
                 description = None, issue =None , category = None, 
                 elements = None , path = None , status = None ):

        t = Objects()

       
        t.id = id
        t.name = name
        t.type = type
        t.description = description
        t.issue = issue
        t.category = category
        t.elemets = elements
        t.path = path
        t.status = status


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
        t = Objects()
        t.id = issue['id'].encode('utf8')
        t.description = issue['description'].encode('utf8')
        t.name = issue['name'].encode('utf8')
        t.order = issue['order'].encode('utf8')


        return t


    def update(self ):


        driveServices = DriveServices()

        aa = driveServices.update_folder(self.id, self.name, self.description)
        print aa
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

