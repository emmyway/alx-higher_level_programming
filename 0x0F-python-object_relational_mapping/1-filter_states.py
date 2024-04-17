#!/usr/bin/python3
import MySQLdb
from sys import argv
'''
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Your code should not be executed when imported
'''


def filter_states(username, password, database):
    # connect to db server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    # create cursor object
    cur = db.cursor()
    # select and filter table
    cur.execute("SELECT * FROM states WHERE name "
                "LIKE 'N%' ORDER BY states.id ASC")
    # fetch rows
    result = cur.fetchall()
    # print result
    for row in result:
        print(row)
    # clean up
    cur.close()
    db.close()


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    filter_states(username, password, database)
