import sqlite3 
from sqlite3 import Error


'''Creacion de BD'''
'''
def sql_connection():
 
    try:
        con = sqlite3.connect('tareasBD.db') 
        print("Connection is established: Database is created in memory")
 
    except Error:
        print(Error)
 
    finally:
        con.close()
 
sql_connection()
'''

'''Crear tablas'''
'''
def sql_connection():
 
    try:
        con = sqlite3.connect('tareasBD.db')
        return con
 
    except Error:
        print(Error)
 
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE tareas(id integer PRIMARY KEY AUTOINCREMENT, tarea text, realizado int)")
    con.commit()
 
con = sql_connection()
 
sql_table(con)
'''

'''Insertar en tabla'''
'''
con = sqlite3.connect('tareasBD.db')
def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO tareas (tarea, realizado) VALUES(?, ?)", entities)
    con.commit()
    print('HE INSERTADO-     ', entities)

entities = ('Tarea flask python', 0)
 
sql_insert(con, entities)

'''

con = sqlite3.connect('tareasBD.db')

def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE tareas SET realizado= 1 where id = 1')
    con.commit()
 
sql_update(con)
