from flask import request, jsonify
from src.domain.user import User
from src.usecase.createUserUseCase import CreateUserUseCase
from src.usecase.listUsersUseCase import ListUsersUseCase
from src.view.dto.userDto import UserDto
from src.dao.mock.userDao import UserDao;

class UserController:

    repository = UserDao()
        
    @staticmethod
    def createUser():
        data = request.json
        # if not UserFormRequest.validate(data):
        #     return jsonify({"error": "Invalid data"}), 400

        createUserCase = CreateUserUseCase(UserController.repository)
        userDto = UserDto()
        userDto.setName(data['name'])
        userDto.setEmail(data['email'])
        userDto.setPassword(data['password'])
        
        response = createUserCase.execute(userDto)
        return jsonify(response.to_dict()), response.getCode()

    @staticmethod
    def listsUsers():        
        listUsersUseCase = ListUsersUseCase(UserController.repository)
        response = listUsersUseCase.execute()
        return jsonify(response.to_dict(), response.getCode())