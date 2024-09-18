class UserDto:
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.password = None
        self.active = None

    def setID(self, id): 
        self.id = id

    def getID(self): 
        return self.id

    def setName(self, name): 
        self.name = name

    def getName(self): 
        return self.name

    def setEmail(self, email): 
        self.email = email

    def getEmail(self): 
        return self.email

    def setPassword(self, password): 
        self.password = password

    def getPassword(self): 
        return self.password

    def setActive(self, active): 
        self.active = active        

    def isActive(self): 
        return self.active 