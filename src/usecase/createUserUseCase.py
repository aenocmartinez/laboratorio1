from src.domain.userRepositoy import UserRepository
from src.view.dto.responseHttp import ResponseHttp
from src.view.dto.userDto import UserDto
from src.domain.user import User

class CreateUserUseCase:
    def __init__(self, UserRepository):
        self.repository = UserRepository

    def execute(self, UserDto):
        response = ResponseHttp()
        user = self.repository.find_user_by_email(UserDto.getEmail())

        if user is not None and user.exists():
            response.setCode(200)
            response.setMessage("El usuario ya existe.")
            return response
        
        
        user = User(self.repository)
        user.setName(UserDto.getName())
        user.setEmail(UserDto.getEmail())
        user.setPassword(UserDto.getPassword())
        user.setActive(True)

        success = user.create()

        if not success:
            response.setCode(500)
            response.setMessage("Ha ocurrido un error en el sistema.")
            return response
        
        response.setCode(201)
        response.setMessage("Usuario creado con éxito")
        return response