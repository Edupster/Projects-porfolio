"""Write the SQL code to create a table called Student. The table structure is
summarised in the table below (Note that STU_NUM is the primary key):"""

CREATE TABLE Student (
    STU_NUM CHAR(6),
    STU_SNAME VARCHAR(15),
    STU_FNAME VARCHAR(15),
    STU_INITIAL CHAR(1),
    STU_STARTDATE DATE,
    COURSE_CODE CHAR(3),
    PROJ_NUM INT(2),
    CONSTRAINT PK_Student PRIMARY KEY (STU_NUM)
);

"""After you have created the table in question 1, write the SQL code to enter
the first two rows of the table as below:"""

INSERT INTO Student
VALUES ('01', 'Snow', 'John', 'E', '05-Apr-14', '201', 6);
INSERT INTO Student
VALUES ('02', 'Stark', 'Arya', 'C', '12-Jul-17', '305', 11);
INSERT INTO Student
VALUES ('03', 'Lannister', 'Jamie', 'C', '05-Sep-12', '101', 2);
INSERT INTO Student
VALUES ('04', 'Lannister', 'Cercei', 'J', '05-Sep-12', '101', 2);
INSERT INTO Student
VALUES ('05', 'Greyjoy', 'Theon', 'I', '09-Dec-12', '402', 14);
INSERT INTO Student
VALUES ('06', 'Tyrell', 'Margaery', 'Y', '12-Jul-17', '305', 10);
INSERT INTO Student
VALUES ('07', 'Baratheon', 'Tommen', 'R', '13-Jun-19', '201', 5);

"""Assuming all the data in the Student table has been entered as shown
below, write the SQL code that will list all attributes for a COURSE_CODE of
305."""

SELECT * FROM [Student]
WHERE COURSE_CODE = 305;


"""Write the SQL code to change the course code to 304 for the person whose
student number is 07."""

UPDATE Student
SET COURSE_CODE = '304'
WHERE STU_NUM = '07';


"""Write the SQL code to delete the row of the person named Jamie Lannister,
who started on 5 September 2012, whose course code is 101 and project
number is 2. Use logical operators to include all of the information given in
this problem."""


DELETE FROM Student WHERE STU_SNAME = 'Lannister' AND STU_FNAME = 'Jamie' AND STU_STARTDATE = '05-Sep-12' AND COURSE_CODE = '101' AND PROJ_NUM = 2;


"""Write the SQL code that will change the PROJ_NUM to 14 for all those
students who started before 1 January 2016 and whose course code is at
least 201."""


UPDATE Student
SET PROJ_NUM = 14
WHERE STU_STARTDATE < '1-January-2016' AND COURSE_CODE >= '201';


"""Write the SQL code that will delete all of the data inside a table, but not the
table itself."""


DELETE FROM Student;


"""Write the SQL code that will delete the Student table entirely."""


DROP TABLE Student;