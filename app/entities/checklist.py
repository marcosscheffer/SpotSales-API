class Checklist():
    def __init__(self, id=None,
                 seller_id=None,
                 sale_date=None,
                 value=None,
                 phases=None,
                 voltage=None,
                 power=None,
                 special_project=None,
                 eletric_key=False,
                 eletric_panel=False,
                 description_panel=None,
                 layout=False,
                 pipeline=False,
                 description_pipeline=None,
                 special_paint=False,
                 extra_filters=False,
                 assembly=None,
                 responsible_assembly=None,
                 freight=None,
                 pallet=False,
                 type_address=None,
                 address=None,
                 deadline=None,
                 other=None,
                 filled=None,
                 ts=None):
        self._id = id
        self._seller_id = seller_id
        self._sale_date = sale_date
        self._value = value
        self._phases = phases
        self._voltage = voltage
        self._power = power
        self._special_project = special_project
        self._eletric_key = eletric_key
        self._eletric_panel = eletric_panel
        self._description_panel = description_panel
        self._layout = layout
        self._pipeline = pipeline
        self._description_pipeline = description_pipeline
        self._special_paint = special_paint
        self._extra_filters = extra_filters
        self._assembly = assembly
        self._responsible_assembly = responsible_assembly
        self._freight = freight
        self._pallet = pallet
        self._type_address = type_address
        self._address = address
        self._deadline = deadline
        self._other = other
        self._filled = filled
        self._ts = ts
        
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
    def phases(self):
        return self._phases
    
    @phases.setter
    def phases(self, phases):
        self._phases = phases
        
    @property
    def voltage(self):
        return self._voltage
    
    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        
    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, power):
        self._power = power
        
    @property
    def special_project(self):
        return self._special_project
    
    @special_project.setter
    def special_project(self, special_project):
        self._special_project = special_project
        
    @property
    def eletric_key(self):
        return self._eletric_key
    
    @eletric_key.setter
    def eletric_key(self, eletric_key):
        self._eletric_key = eletric_key
        
    @property
    def eletric_panel(self):
        return self._eletric_panel
    
    @eletric_panel.setter
    def eletric_panel(self, eletric_panel):
        self._eletric_panel = eletric_panel
        
    @property
    def description_panel(self):
        return self._description_panel
    
    @description_panel.setter
    def description_panel(self, description_panel):
        self._description_panel = description_panel
        
    
    @property
    def layout(self):
        return self._layout
    
    @layout.setter
    def layout(self, layout):
        self._layout = layout
        
    
    @property
    def pipeline(self):
        return self._pipeline
    
    @pipeline.setter
    def pipeline(self, pipeline):
        self._pipeline = pipeline
        
    @property
    def description_pipeline(self):
        return self._description_pipeline
    
    @description_pipeline.setter
    def description_pipeline(self, description_pipeline):
        self._description_pipeline = description_pipeline
        
    
    @property
    def special_paint(self):
        return self._special_paint
    
    @special_paint.setter
    def special_paint(self, special_paint):
        self._special_paint = special_paint
        
    
    @property
    def extra_filters(self):
        return self._extra_filters
    
    @extra_filters.setter
    def extra_filters(self, extra_filters):
        self._extra_filters = extra_filters
        
    @property
    def assembly(self):
        return self._assembly
    
    @assembly.setter
    def assembly(self, assembly):
        self._assembly = assembly
        
    @property
    def responsible_assembly(self):
        return self._responsible_assembly
    
    @responsible_assembly.setter
    def responsible_assembly(self, responsible_assembly):
        self._responsible_assembly = responsible_assembly
        
    
    @property
    def freight(self):
        return self._freight
    
    @freight.setter
    def freight(self, freight):
        self._freight = freight
        
    
    @property
    def pallet(self):
        return self._pallet
    
    @pallet.setter
    def pallet(self, pallet):
        self._pallet = pallet
        
    @property
    def type_address(self):
        return self._type_address
    
    @type_address.setter
    def type_address(self, type_address):
        self._type_address = type_address    
        
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address
        
    
    @property
    def deadline(self):
        return self._deadline
    
    @deadline.setter
    def deadline(self, deadline):
        self._deadline = deadline
        
    
    @property
    def other(self):
        return self._other
    
    @other.setter
    def other(self, other):
        self._other = other
        
    
    @property
    def filled(self):
        return self._filled
    
    @filled.setter
    def filled(self, filled):
        self._filled = filled
        
    @property
    def ts(self):
        return self._ts
    
    @ts.setter
    def ts(self, ts):
        self._ts = ts
    