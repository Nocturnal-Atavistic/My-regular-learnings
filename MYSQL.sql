CREATE DATABASE WSCUBE
USE WSCUBE

CREATE TABLE USERS
(
	id int unsigned,
    name varchar(100),
    email varchar(150),
    password varchar(100),
    contact varchar(15),
    address text,
    Dob date,
    gender enum("m", "F", "O"),
    status boolean

)

INSERT INTO USERS
VALUES
(1, "kimmm", "kimm@gmial.com", "12485678", "98949745866","Dubai" ,"1999-01-01", "f", 1 ),
(2, "Mehta", "mehta@gmail.com", "53535325", "980878978", "india", "1998-07-25", "M", 1)
