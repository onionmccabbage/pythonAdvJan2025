import sqlite3

def customRead(w='r'):
    '''retrieve matching members from the DB table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # NB in SQL we may use double-quotes or single quotes for string content
    # WHERE creature = "{w}" # finds an exact match
    # WHERE creature LIKE "{w}%" # find anything begining with...
    # WHERE creature LIKE "%{w}%" # finds anything containing...
    st = f'''
    SELECT creature, count, cost FROM zoo
    WHERE creature LIKE "%{w}%"
'''
    try:
        curs.execute(st)
        conn.commit()
        rows = curs.fetchall()
        conn.close()
        return rows
    except Exception as err:
        print(err)

if __name__ == '__main__':
    w = customRead()
    print(w)