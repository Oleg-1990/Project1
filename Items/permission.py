from Service import role_service, user_service


class Permission:
    def __init__(self):
        self.role_service = role_service
        self.user_service = user_service

    # function about User
    
    def add_user(self):
        pass

    def delete_user(self):
        pass

    def update_user(self):
        pass

    def find_user(self):
        pass

    def find_all_users(self):
        pass

    # function about Role
    def add_role(self):
        pass

    def delete_role(self):
        pass

    def update_role(self):
        pass