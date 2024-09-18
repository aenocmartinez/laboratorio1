from abc import ABC, abstractmethod

class UserRepository(ABC):
    def create_user(self, user):
        pass

    def find_user_by_email(self, email):
        pass

    def find_user_by_id(self, id): 
        pass

    def active_user(self, id): 
        pass

    def inactive_user(self, id):
        pass

    def all_users(self):
        pass