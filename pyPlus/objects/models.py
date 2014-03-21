import json

from ..core import r
from ..helpers import JsonSerializer, DriveServices
from ..settings import FILESTORETMP

class ObjectJsonSerializer(JsonSerializer):
    __json_hidden__ = ['strategy']
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
    def save(self , parent_id = None , filename = None ):
        driveServices = DriveServices()
        
        if parent_id == None:
            parent_id = self.__object__.issue
        
        if filename == None:
            filename = "image.png"
        filename = FILESTORETMP + filename
        
        fileT = driveServices.insert_file( self.__object__.name , 
                                   self.__object__.description, 
                                   parent_id, filename)
        self.__object__.id = fileT['id']
        
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
        driveServices = DriveServices()
        folde = driveServices.create_folder( self.__object__.name, 
                                             self.__object__.description, 
                                             self.__object__.issue)
        return folde

    def update(self):
        
        driveServices = DriveServices()

        folde = driveServices.update_folder(self.__object__.id, 
                                            self.__object__.name, 
                                            self.__object__.description)
        return folde
    
    def save(self):
        driveServices = DriveServices()
        folde = driveServices.create_folder( self.__object__.name, 
                                             self.__object__.description, 
                                             self.__object__.issue)
        
        self.__object__.id = folde['id']
        
        return folde

    def get(self):
        driveServices = DriveServices()
        
        fileT = driveServices.get_file(self.__object__.id)
        return fileT
        
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
         
         
    
    def __init__(self , id = None , name = None , _typeO = None, 
                 description = None, issue =None , category = None, 
                 elemets = None , path = None , status = None ):
        
        
        self.id = id
        self.name = name
        self.typeO = _typeO
        self.description = description
        self.issue = issue
        self.category = category
        self.elemets = elemets
        self.path = path
        self.status = status

    @classmethod
    def new(self , id = None , name = None , _typeO = None, 
                 description = None, issue =None , category = None, 
                 elements = None , path = None , status = None ):

        t = Objects()

       
        t.id = id
        t.name = name
        t.typeO = _typeO
        t.description = description
        t.issue = issue
        t.category = category
        t.elemets = elements
        t.path = path
        t.status = status


        return t
    

    def save(self):
        print "Entramos a Object model save"
        driveServices = DriveServices()
        #crear un achivo para subirlo...
        # tomar la categoria,
        
        self.strategy.save()
        
        r.hset("object", self.id, json.dumps(self.to_json()))

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

        issue = json.loads(r.hget("object",id))
        print issue
        t = Objects(**issue)

            
        return t


    def update(self ):


        driveServices = DriveServices()

        aa = driveServices.update_folder(self.id, self.name, self.description)


        r.hset("object", self.id, json.dumps(self.to_json()))

        return self

    @classmethod
    def delete(self , id=None):
        driveServices = DriveServices()

        if id != None:
            self.id = id

        if self.id != None:
            driveServices.delete_file(self.id)
            r.hdel("object" ,self.id )
            return True

        return False

