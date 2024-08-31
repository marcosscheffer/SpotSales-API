class FilterOp:
    def __init__(self, id, seller_id, sale_date, value, ts, deadline=None, carrier=None):
        self._id = id
        self._seller_id = seller_id
        self._sale_date = sale_date
        self._value = value
        self._ts = ts
        self._deadline = deadline
        self._carrier = carrier
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
        
    @property
    def seller_id(self):
        return self._seller_id
    
    @seller_id.setter
    def seller_id(self, seller_id):
        self._seller_id = seller_id
        
    
    @property
    def sale_date(self):
        return self._sale_date
    
    @sale_date.setter
    def sale_date(self, sale_date):
        self._sale_date = sale_date
        
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
        
    
    @property
    def ts(self):
        return self._ts
    
    @ts.setter
    def ts(self, ts):
        self._ts = ts
        
        
    @property
    def deadline(self):
        return self._deadline
    
    @deadline.setter
    def deadline(self, deadline):
        self._deadline = deadline
    
    
    @property
    def carrier(self):
        return self._carrier
    
    @carrier.setter
    def carrier(self, carrier):
        self._carrier = carrier