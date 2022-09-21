DROP TABLE IF EXISTS students;

CREATE TABLE students (
    stud_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    stud_fname TEXT NOT NULL,
    stud_mname TEXT,
    stud_lname TEXT NOT NULL,
    stud_dob DATE NOT NULL,
    stud_course TEXT NOT NULL,
    stud_year TEXT NOT NULL,
    stud_email TEXT NOT NULL,
    stud_contact TEXT NOT NULL,
    stud_address TEXT NOT NULL
);