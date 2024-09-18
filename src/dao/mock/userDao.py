from src.domain.userRepositoy import UserRepository

class UserDao(UserRepository):
    def __init__(self):
        self.users = []
    
    def create_user(self, user):
        self.users.append(user)
        return True

    def find_user_by_email(self, email):
        for u in self.users:
            if u.getEmail() == email:
                return u
        return None

    def find_user_by_id(self, id): 
        for user in self.users:
            if user.getID () == id:
                return user
        return None

    def active_user(self, id): 
        user = self.find_user_by_id(id)
        if user.exists():
            print(f"el usuario {user.getName()} existe se puede activar")
            user.setActive(True)

    def inactive_user(self, id):
        user = self.find_user_by_id(id)
        if user.exists():
            print(f"el usuario {user.getName()} existe se puede inactivar")
            user.setActive(False)

    def all_users(self):
        return self.users