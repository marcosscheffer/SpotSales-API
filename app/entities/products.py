class Product:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id