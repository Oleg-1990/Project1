Необходимо создать сущности и соответствующие таблицы в БД - Users, Roles, Permissions.
У User есть логин(уникальное поле), пароль, Role, личная информация(имя, фамилия и электронная почта).
У Role есть название и список ассоциируемых с ней Permission.
У Permission есть название.
В системе должно быть два типа пользователей: admin, client.

Смотреть файлы в пап Task
Реализовать:

    CRUD операции над всеми сущностями.
    поиск пользователь по имени;
    выборка пользователей с поддержкой пейджинации и сортировки по имени/фамилии;
    аутентификация(по сути поиск пользователя по имени и паролю).