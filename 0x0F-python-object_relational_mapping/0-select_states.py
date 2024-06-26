#!/usr/bin/python3
'''
A script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
'''

import MySQLdb
import sys


def list_states(username, password, database):
    '''
    script lists all rows in table (state)
    Args:
        username: the mysql server username
        password: the password to mysql server
        database: the database name
    '''
    # connect to mysql database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    # creating the cursor object
    cur = db.cursor()
    # selecting all states row
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    # fetching all
    output = cur.fetchall()
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
