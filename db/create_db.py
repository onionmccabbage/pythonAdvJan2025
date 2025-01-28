import sqlite3 # this database is part of the Python standard library

def createDB():
    '''create a database and also a table within it'''
    conn = sqlite3.connect('my_db') # connect or create
    curs = conn.cursor()
    # write a SQL statement (plain text)
    st ='''
    CREATE TABLE zoo
    (
        creature VARCHAR(32) PRIMARY KEY,
        count int,
        cost float
    )
'''
    # execute the SQL statement
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print(f'There was a problem: {err}')

    # always a good idea to release resources when done
    conn.close()

if __name__ == '__main__':
    createDB()