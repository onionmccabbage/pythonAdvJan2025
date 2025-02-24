import sqlite3

def main():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = '''
    SELECT userID, id, title, completed FROM todos;
    '''
    # execute
    try:
        curs.execute(st)
        rows = curs.fetchall()
    except Exception as err:
        print('There was a problem:{}'.format(err))
    finally:
        conn.close() # always make sure the connection is closed

    # we can explore the 'rows'
    for item in rows:
        if item[3] == 1:
            phrase = ''
        else:
            phrase ='not'
        print('Item {} (user {}) title:{} is {} completed'
            .format(item[1], item[0], item[2], phrase))

if __name__ == '__main__':
    main()