class User:
    def __init__(self, name, email, cpf, password, position_id, active=False):
        self._name = name
        self._email = email
        self._cpf = cpf
        self._password = password
        self._position_id = position_id
        self._active = active
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
       
        
    @property
    def position_id(self):
        return self._position_id
    
    @position_id.setter
    def position_id(self, position_id):
        self._position_id = position_id
        
        
    @property
    def active(self):
        return self._active
    
    @active.setter
    def active(self, active):
        self._active = active