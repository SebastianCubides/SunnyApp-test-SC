class DataImport:
    def __init__(self):
        with open("datos.txt") as f:
            self.lines = f.readlines() 
    
    def getData(self):
        return self.lines