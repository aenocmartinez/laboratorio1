from flask import request, jsonify
from src.domain.user import User
from src.usecase.createUserUseCase import CreateUserUseCase
from src.usecase.listUsersUseCase import ListUsersUseCase
from src.view.dto.userDto import UserDto
from src.dao.mock.userDao import UserDao


class UserController:

    repository = UserDao() #Instancia de la clase UserDao

    @staticmethod
    def createUser():
        data = request.json # Se obtiene el cuerpo de la solicitud HTTP 
        # if not UserFormRequest.validate(data):
        #     return jsonify({"error": "Invalid data"}), 400

        createUserCase = CreateUserUseCase(UserController.repository) # Se crea un objeto CreateUserUseCase con la instancia de UserDao
        userDto = UserDto() #Se crea el objeto con los atributos (name, email y pass)
        userDto.setName(data["name"])
        userDto.setEmail(data["email"])
        userDto.setPassword(data["password"])

        response = createUserCase.execute(userDto) # creo que se llama el usuario
        return jsonify(response.to_dict()), response.getCode()

    @staticmethod
    def listsUsers(): # Método para listar las solicitudes de user
        listUsersUseCase = ListUsersUseCase(UserController.repository)
        response = listUsersUseCase.execute()
        return jsonify(response.to_dict(), response.getCode())
