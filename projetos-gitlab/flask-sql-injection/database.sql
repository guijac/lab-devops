CREATE DATABASE my_database;
use my_database;

CREATE TABLE users (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL
);

INSERT INTO users VALUES (null,"teste@teste.com","1234");
INSERT INTO users VALUES (null,"teste2@teste.com","1234");
INSERT INTO users VALUES (null,"teste3@teste.com","supersenha");
INSERT INTO users VALUES (null,"teste4@teste.com","souhacker");