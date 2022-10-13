CREATE DATABASE  postgres;
\c postgres;
CREATE TABLE user(
user_login VARCHAR(30) PRIMARY KEY,
user_password VARCHAR(30),
user_role VARCHAR(5) FOREIGN KEY,
user_name VARCHAR(30),
user_surname VARCHAR(30),
user_email VARCHAR(30)
);


