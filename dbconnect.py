import pymysql
from os import environ

def get_connection():
    return pymysql.connect(host=environ['DB_HOST'], port=int(environ['DB_PORT']), user=environ['DB_USER'], passwd=environ['DB_PASSWORD'], db=environ['DB_NAME'])

def execute_query(q, val=None):
    con = get_connection()
    cmd = con.cursor()
    if val:
        cmd.execute(q, val)
    else:
        cmd.execute(q)
    con.commit()
    return cmd

def iud(q, val):
    cmd = execute_query(q, val)
    return cmd.lastrowid

def select(q, val=None):
    cmd = execute_query(q, val)
    return cmd.fetchall()

def selectall(q, val=None):
    cmd = execute_query(q, val)
    return cmd.fetchall()

def selectone(q, val=None):
    cmd = execute_query(q, val)
    return cmd.fetchone()

def androselectall(q):
    cmd = execute_query(q)
    s = cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = [dict(zip(row_headers, result)) for result in s]
    return json_data

def androselectalls(q, val):
    cmd = execute_query(q, val)
    s = cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = [dict(zip(row_headers, result)) for result in s]
    return json_data

