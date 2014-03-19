import json

from ..core import r
from ..helpers import JsonSerializer, DriveServices


class ObjectJsonSerializer(JsonSerializer):
    pass

class Article():
    __object__ = None
    
    def __init__(self, objectT):
        self.__object__ = objectT
        
    def new(self):
        pass
    def save(self):
        pass
    def all(self ):
        pass
    def get(self):
        pass
    def delete(self):
        pass



class Image():
    __object__ = None
    
    def __init__(self, objectT):
        self.__object__ = objectT
        
    def new(self):
        pass
    def save(self):
        pass
    def all(self ):
        pass
    def get(self):
        pass
    def delete(self):
        pass
  

class Dossier():
    
    __object__ = None
    
    def __init__(self, objectT):
        self.__object__ = objectT
    
    def new(self):
        pass
    def save(self):
        pass
    def all(self ):
        pass
    def get(self):
        pass
    def delete(self):
        pass

class Objects(ObjectJsonSerializer):

    id = None
    name = None
    _typeO = None
    description = None
    issue = None
    category = None
    elemets = None
    path = None
    status = None
    strategy = None
    

    @property
    def typeO(self):
        
        if self._typeO == None:
            self._typeO = "Dossier"
            self.strategy = Dossier(self)
        
        return self._typeO
    
    
    @typeO.setter
    def typeO(self,value):
        
        
        if value == "Dossier":
            self.strategy = Dossier(self)
            
        if value == "Article":
            self.strategy = Article(self)
            
        if value == "Image":
            self.strategy = Image(self)
        
        
        self._typeO = value
        
        
    @typeO.deleter
    def typeO(self):
        del self._typeO
         
         
    
    def __init__(self , id = None , name = None , typeO = None, 
                 description = None, issue =None , category = None, 
                 elements = None , path = None , status = None ):
        
        
        self.id = id
        self.name = name
        self.typeO = typeO
        self.description = description
        self.issue = issue
        self.category = category
        self.elemets = elements
        self.path = path
        self.status = status

    @classmethod
    def new(self , id = None , name = None , typeO = None, 
                 description = None, issue =None , category = None, 
                 elements = None , path = None , status = None ):

        t = Objects()

       
        t.id = id
        t.name = name
        t.typeO = typeO
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
        #crear un achivo para subirlo...
        # tomar la categoria,
        
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

