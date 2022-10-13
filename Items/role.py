import permission as Pe


class Client:
    def __init__(self):
        self.find_user = Pe.Permission.find_user


class Admin:
    def __init__(self):
        pass