#
# Grant Bossa
# April 26, 2025
# Relational Database Programming Project
# SDEV 1200
#
# fmt: off
'''# Instructions 

In this assignment, you will create a database named `student_info.db` that holds 
the following information about students at a college:

* The student's name
* The student's major
* The department in which the student is enrolled 

The database should have the following tables:

### Majors Table

| Column Name | Data Type |
| ----------- | --------- |
| MajorID | INTEGER PRIMARY KEY |
| Name | TEXT |

### Departments Table

| Column Name | Data Type |
| ----------- | --------- |
| DeptID | INTEGER PRIMARY KEY |
| Name | TEXT |

### Students Table

| Column Name | Data Type |
| ----------- | --------- |
| StudentID | INTEGER PRIMARY KEY |
| Name | TEXT |
| MajorID | INTEGER (Foreign key that references the MajorID column in the Majors table) |
| DeptID | INTEGER (Foreign key that references the DeptID column in the Departments table) |
'''
# fmt: on

import sqlite3


def main():
    # Connect to the database.
    conn = sqlite3.connect("student_info.db")

    # Get a database cursor.
    cur = conn.cursor()

    # -----------------------------------------------------------------------------------
    # Add the Majors table.
    add_majors_table(cur)

    # -----------------------------------------------------------------------------------
    # Add the Departments table.
    add_departments_table(cur)

    # -----------------------------------------------------------------------------------
    # Add the Students table.
    add_students_table(cur)

    # -----------------------------------------------------------------------------------

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# The add_majors_table adds the Majors table to the database.
def add_majors_table(cur):
    # If the table already exists, drop it.
    cur.execute("DROP TABLE IF EXISTS Majors")

    # Create the table.
    cur.execute(
        """CREATE TABLE Majors (MajorID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT)"""
    )


# The add_departments_table adds the Departments table to the database.
def add_departments_table(cur):
    # If the table already exists, drop it.
    cur.execute("DROP TABLE IF EXISTS Departments")

    # Create the table.
    cur.execute(
        """CREATE TABLE Departments (DeptID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT)"""
    )


# The add_students_table adds the Students table to the database.
def add_students_table(cur):
    # If the table already exists, drop it.
    cur.execute("DROP TABLE IF EXISTS Students")

    # Create the table.
    cur.execute(
        """CREATE TABLE Students (StudentID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        MajorID INTEGER REFERENCES Majors(MajorID),
                                        DeptID INTEGER REFERENCES Department(DeptID)
                )"""
    )


# Execute the main function.
if __name__ == "__main__":
    main()
