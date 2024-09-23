from abc import ABC, abstractmethod

#UserRepository -> Clase abstracta que establece un contrato para las operaciones relacionadas con los usuarios
class UserRepository(ABC):
    #Se crea un nuevo User
    def create_user(self, user):
        pass
    #Se busca un User por su correo electrónico
    def find_user_by_email(self, email):
        pass
    #Se busca un usuario por su ID
    def find_user_by_id(self, id):
        pass
    #Activa User
    def active_user(self, id):
        pass
    #Desactiva User
    def inactive_user(self, id):
        pass
    #Obtiene todos los usuarios creados con las respectivas funciones anteriores
    def all_users(self):
        pass
