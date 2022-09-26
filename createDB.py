### import library for reading the code
import sqlite3

## connecting to sqlite
## connecting to object
connect = sqlite3.connect('patients.db')

## db object
db = connect.cursor()

## delete existing patients' table
db.execute('DROP TABLE IF EXISTS patients.db')
connect.commit

## create table in database
table = """ CREATE TABLE patient_table (
    idnumber VARCHAR(225) NOT NULL,
    sex CHAR(25) NOT NULL,
    email CHAR(25) NOT NULL,
    phonenumber CHAR(25) NOT NULL
    );"""

db.execute(table)
connect.commit()

## insert data into table
db.execute("INSERT INTO patient_table(idnumber, sex, email, phonenumber) values('1234', 'Male', 'john@gmail.com', '3471215050')")
db.execute("INSERT INTO patient_table(idnumber, sex, email, phonenumber) values('1235', 'Female', 'mary@gmail.com', '6311215050')")
db.execute("INSERT INTO patient_table(idnumber, sex, email, phonenumber) values('1236', 'Male', 'peter@gmail.com', '2011215270')")
db.execute("INSERT INTO patient_table(idnumber, sex, email, phonenumber) values('1237', 'Female', 'sarah@gmail.com', '2021218090')")

connect.commit()

## close the connection
connect.close