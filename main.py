from Service import user_service as serv
from Items import user

if __name__ == '__main__':
    oleg = user.User('Olleg90', '$#jklfh90', 'admin', 'oleg', 'Skorodielov', 'skorodelov90@gmail.com')
    s = serv.UserService()
    s.add(oleg)


