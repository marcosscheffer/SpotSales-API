class User:
    def __init__(self, name=None, email=None, cpf=None, password=None, position_id=None, 
                 active=False, admin=False, bot=False):
        self._name = name
        self._email = email
        self._cpf = cpf
        self._password = password
        self._position_id = position_id
        self._active = active
        self._admin = admin
        self._bot = bot
        
        
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
        
        
    @property
    def admin(self):
        return self._admin
    
    @admin.setter
    def admin(self, admin):
        self._admin = admin
        
    
    @property
    def bot(self):
        return self._bot
    
    @bot.setter
    def bot(self, bot):
        self._bot = bot