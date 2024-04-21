#!/usr/bin/python3
'''
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
Your script should take 4 arguments: mysql username, mysql
password, database name and state name searched
(no argumentvalidation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Your code should not be executed when imported
'''

import MySQLdb
from sys import argv
import sys


def match_list(username, password, database, state_name):
    '''
    prints state info that matches name argument
    Args:
        username: the mysql server username
        password: the password to mysql server
        database: the database name
    '''
    # est conneftion to db server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, db=database)
    # create cursor object
    cur = db.cursor()
    # select table and match
    query = "SELECT * FROM states WHERE name = '{}'
    ORDER BY id ASC".format(state_name)
    cur.execute(query)
    # fetch result
    result = cur.fetchall()
    # print result
    for row in result:
        print(row)
    # clean up
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        sys.exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    match_list(username, password, database, state_name)
