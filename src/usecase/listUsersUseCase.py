from src.domain.userRepositoy import UserRepository
from src.view.dto.responseHttp import ResponseHttp

class ListUsersUseCase:

    def __init__(self, UserRepository):
        self.repository = UserRepository

    def execute(self):
        users = self.repository.all_users()

        users_dict = [user.to_dict() for user in users]

        response = ResponseHttp()
        
        response.setCode(200)
        response.setData(users_dict)
        return response
        