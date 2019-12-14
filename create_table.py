import os
import sqlite3
from sqlite3 import Error

#Clear student_gpa.db if exists
if os.path.exists('student_gpa.db'):
        os.remove('student_gpa.db') 

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
 
 
def create_project(conn, data):
    """
    Insert data into the student_gpa table
    :param conn:
    :param data:
    """

    sql = ''' INSERT INTO student_gpa(last_name,first_name,gpa,student_id)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
 
def main():
    database = r"student_gpa.db"
 
    # create a database connection
    conn = create_connection(database)

    student_gpa = """ CREATE TABLE IF NOT EXISTS student_gpa (
                                        last_name VARCHAR(100),
                                        first_name VARCHAR(100),
                                        gpa VARCHAR(10),
                                        student_id VARCHAR(15) PRIMARY KEY,
                                        version INTEGER DEFAULT 1
                                    ); """
    # create table
    if conn is not None:
        # create student_gpa table
        create_table(conn, student_gpa)
    else:
        print("Error! cannot create the database connection.")

    with conn:
        # populate table
        for i in range(8):
            data = ('Lastname' + str(i), 'Firstname' + str(i), str(3.0 + i/10), 3 * str(i) + '-' + 2 * str(i + 1) + '-' + 4 * str(i +2))
            create_project(conn, data)
 
if __name__ == '__main__':
    main()