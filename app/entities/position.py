class Position:
    def __init__(self, title):
        self._title = title
    
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    