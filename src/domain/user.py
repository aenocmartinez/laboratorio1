from src.domain.userRepositoy import UserRepository


class User:
    def __init__(self, UserRepository):
        self.id = None
        self.name = None
        self.email = None
        self.password = None
        self.active = True
        self.repository = UserRepository # Inyeccion de dependencias (creo)

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
        return self.id > 0 # Si el id es mayor a 0, el usuario existe

    def create(self):
        return self.repository.create_user(self) # Crea un nuevo usuario

    def to_dict(self): #Se convierte el objeto (user) a un diccionario de datos
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
