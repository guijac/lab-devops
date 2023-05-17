CREATE DATABASE my_database;
use my_database;

CREATE TABLE user (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL
);

INSERT INTO user VALUES (null,"teste@teste.com","12345678");
INSERT INTO user VALUES (null,"teste2@teste.com","87654321");
INSERT INTO user VALUES (null,"teste3@teste.com","supersenha");
INSERT INTO user VALUES (null,"teste4@teste.com","souhacker");