from Repository import repository
from Items import user, role



class UserService:
    def __init__(self):
        self.repo = repository

    def add(self, user: user.User):
        self.repo.insert_into_user(user.login, user.password, user.role, user.name, user.surname, user.email)

    def find_all(self):
        self.repo.select_all_users()

