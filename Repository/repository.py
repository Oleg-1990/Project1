import psycopg2
from Constants import constants as c

connect = psycopg2.connect(dbname=c.postgres.name, user=c.postgres.user, password=c.postgres.password,
                           host=c.postgres.host, port=c.postgres.port)
cursor = connect.cursor()


def select_all_users():
    cursor.execute("select * from user")
    users = cursor.fetchall()
    for user in users:
        print(user)


def insert_into_user(login: str, password: str, role: str, name: str, surname: str, email: str):
    cursor.execute(f"insert into user(user_login, user_password, user_role, user_name,user_surname,user_email) "
                   f"values('{login}', '{password}', {role}, {name}, {surname}, {email})")
