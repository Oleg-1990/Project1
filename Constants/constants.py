from collections import namedtuple

db_connect_constants = namedtuple('Connection', ['name', 'user', 'password', 'host', 'port'])
postgres = db_connect_constants('postgres', 'user', 'password', 'localhost', '5432')

