class ProductSold:
    def __init__(self, product_id, filter_op_id, description, quantity ):
        self._product_id = product_id
        self._filter_op_id = filter_op_id
        self._description = description
        self._quantity = quantity
        
    @property
    def product_id(self):
        return self._product_id
    
    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id
        
        
    @property
    def filter_op_id(self):
        return self._filter_op_id
    
    @filter_op_id.setter
    def filter_op_id(self, filter_op_id):
        self._filter_op_id = filter_op_id
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
        
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity
        