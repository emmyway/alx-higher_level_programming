#!/usr/bin/env python3
import MySQLdb
import sys
'''
python script to manipulate a database table
'''
def list_states(username, password, database):
    '''
    script lists all rows in table (state)
    '''
    # connect to mysql database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    # creating the cursor object
    cur = db.cursor()
    # selecting all states row
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    # fetching all
    output  = cur.fetchall()
    # printing states
    for state in output:
        print(state)
    # cleaning up
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)


