from src.domain.userRepositoy import UserRepository

class User:
    def __init__(self, UserRepository):
        self.id = None
        self.name = None
        self.email = None
        self.password = None
        self.active = True
        self.repository = UserRepository

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
    
    def getActive(self):
        return self.active
    
    def exists(self):
        return self.id > 0
    
    def create(self): 
        return self.repository.create_user(self)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,            
        }