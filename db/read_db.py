import sqlite3

def readDB():
    ''' read back all the data from the DB table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # SELECT * is permissible but we tend to use explicit field names
    # the terminating ; ends the SQL statement (reduces the risk of injection attacks)
    st = '''
    SELECT creature, count, cost FROM zoo;
'''
    try:
        curs.execute(st)
        conn.commit()
        # we may now read back from the cursor
        rows = curs.fetchall()
        conn.close()
        return rows
    except Exception as err: # we may have multiple exception handlers, each for a possible exception type
        print(err)

if __name__ == '__main__':
    r = readDB()
    print(r, type(r))
    # we may choose to iterate over the result
    for animal in r:
        #                                                       format float to 2dp
        print(f'We have {animal[1]} {animal[0]} each costing {animal[2]:.2f}')