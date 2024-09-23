from src.domain.userRepositoy import UserRepository  # Importa la clase UserRepository

class UserDao(UserRepository):  # Define la clase UserDao que hereda de UserRepository
    def __init__(self):
        self.users = []  # Inicializa una lista vacía para almacenar usuarios

    def create_user(self, user):
        self.users.append(user)  # Se agrega un nuevo usuario a la lista
        return True  # Retorna True indicando que la creación fue exitosa

    def find_user_by_email(self, email):
        for u in self.users:  # Itera sobre la lista de usuarios
            if u.getEmail() == email:
                return u  #Devuelve el usuario encontrado o si su correo electronico coincide
        return None

    def find_user_by_id(self, id):
        for user in self.users:  # Itera sobre la lista de usuarios
            if user.getID() == id:  # Verifica si el ID coincide
                return user  # Retorna el usuario encontrado
        return None

    def active_user(self, id):
        user = self.find_user_by_id(id)  # Busca el usuario por ID
        if user.exists():  # Verifica si el usuario existe
            print(f"el usuario {user.getName()} existe se puede activar")
            user.setActive(True) #

    def inactive_user(self, id):
        user = self.find_user_by_id(id)
        if user.exists():
            print(f"el usuario {user.getName()} existe se puede inactivar")
            user.setActive(False)

    def all_users(self):
        return self.users  # Retorna la lista de todos los usuarios
