import sqlite3

def customUpdate(w):
    '''Update matching rows in the DB'''
    count = int(float(w['count']))
    creature = w['creature']
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = f'''
    UPDATE zoo
    SET count={count}
    WHERE creature LIKE "%{creature}%";
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
         # we could see teh affected rows e.g. rows=curs.fetchAll()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    w = {'creature':'Penguin', 'count':129}
    customUpdate(w)