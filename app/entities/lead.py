class Lead:
    def __init__(self, id, phone1, phone2, company, city, state):
        self._id = id
        self._phone1 = phone1
        self._phone2 = phone2
        self._city = city
        self._company = company
        self._state = state
        
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    
    @property
    def phone1(self):
        return self._phone1
    
    @phone1.setter
    def phone1(self, phone1):
        self._phone1 = phone1
        
    
    @property
    def phone2(self):
        return self._phone2
    
    @phone2.setter
    def phone2(self, phone2):
        self._phone2 = phone2
        
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        self._city = city
        
    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, company):
        self._company = company
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        self._state = state     
    