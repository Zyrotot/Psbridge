CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE IF NOT EXISTS deviceTickets (
    id int NOT NULL AUTO_INCREMENT,
    ticket int,
    tipo enum('dispositivo', 'circuito'),
    ip varchar(255),
    aberto bool NOT NULL,
    tempo datetime,
    PRIMARY KEY (ID)
);