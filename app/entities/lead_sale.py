class LeadSale:
    def __init__(self, id, company, sale_date, value, seller_id, ts, filter, filled=None):
        self._id = id
        self._sale_date = sale_date
        self._value = value
        self._seller_id = seller_id
        self._company = company
        self._ts = ts
        self._filter = filter
        self._filled = filled
        
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    
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
    def seller_id(self):
        return self._seller_id
    
    @seller_id.setter
    def seller_id(self, seller_id):
        self._seller_id = seller_id
        
    
    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, company):
        self._company = company
        
        
        
    @property
    def ts(self):
        return self._ts
    
    @ts.setter
    def ts(self, ts):
        self._ts = ts
        
    @property
    def filter(self):
        return self._filter
    
    @filter.setter
    def filter(self, filter):
        self._filter = filter
        
    @property
    def filled(self):
        return self._filled
    
    @filled.setter
    def filled(self, filled):
        self._filled = filled
        
    