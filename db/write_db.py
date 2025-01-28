import sqlite3

def writeDB():
    '''write a single entry to the new database table'''
    conn = sqlite3.connect('my_db') # this code is common across many modules
    curs = conn.cursor()
    # SQL statement
    st = '''
    INSERT INTO zoo
    VALUES ("Penguin", 16, 0.52);
''' 
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(f'{err}')

if __name__ == '__main__':
    writeDB()