from src.domain.userRepositoy import UserRepository
from src.view.dto.responseHttp import ResponseHttp

# ListUsersUseCase -> Se encarga de listar todos los usuarios
class ListUsersUseCase:

    def __init__(self, UserRepository):
        self.repository = UserRepository

    def execute(self):
        users = self.repository.all_users()

        users_dict = [user.to_dict() for user in users] # Se convierte el objeto (user) a un diccionario de datos

        response = ResponseHttp() # Se crea un objeto ResponseHttp para manejar la respuesta HTTP

        response.setCode(200) # Si se listan los usuarios, se retorna un mensaje de éxito
        response.setData(users_dict)
        return response
