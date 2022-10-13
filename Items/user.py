
class User:
    def __init__(self, login, password, role, name, surname, email ):
        self.login = login
        self.password = password
        self.role = role
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        print(f'login:{self.login},password:{self.password}, role:{self.role}, '
              f'name:{self.name}, surname:{self.surname}, email:{self.email}')
