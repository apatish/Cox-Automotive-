import sqlite3
from sqlite3 import Error

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


def sql_query(query):
    conn = create_connection(r"student_gpa.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    conn = create_connection(r"student_gpa.db")
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    conn = create_connection(r"student_gpa.db")
    cur = conn.cursor()
    print(query + ' ' + str(var))
    cur.execute(query,var)
    conn.commit()

def sql_query2(query,var):
    conn = create_connection(r"student_gpa.db")
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows