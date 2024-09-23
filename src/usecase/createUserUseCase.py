from src.domain.userRepositoy import UserRepository
from src.view.dto.responseHttp import ResponseHttp
from src.view.dto.userDto import UserDto
from src.domain.user import User


class CreateUserUseCase:
    def __init__(self, UserRepository): #Constructor de la clase que recibe como objeto UserRepository
        self.repository = UserRepository

    def execute(self, UserDto): #UserDto contiene la información del nuevo usuario
        response = ResponseHttp() # Se crea un objeto ResponseHttp para manejar la respuesta HTTP
        user = self.repository.find_user_by_email(UserDto.getEmail()) # Busca un usuario por su correo electrónico

        if user is not None and user.exists(): # Si el usuario existe, se retorna un mensaje de usuario registrado
            response.setCode(200)
            response.setMessage("El usuario ya existe.")
            return response

        # Si el usuario no existe, se crea un nuevo usuario con los atributos del UserDto
        user = User(self.repository)
        user.setName(UserDto.getName())
        user.setEmail(UserDto.getEmail())
        user.setPassword(UserDto.getPassword())
        user.setActive(True)

        success = user.create() # Se crea el nuevo usuario

        if not success: # Si no se crea el usuario, se retorna un mensaje de error
            response.setCode(500)
            response.setMessage("Ha ocurrido un error en el sistema.")
            return response

        response.setCode(201) # Si se crea el usuario, se retorna un mensaje de éxito
        response.setMessage("Usuario creado con éxito")
        return response
