#!/usr/bin/python3
'''
a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Your code should not be executed when imported
'''
import MySQLdb
import sys


def no_injection(username, password, database, state_name):
    '''
    functon searches prints a given state arg from a database,
    not giving room for sql injection
    Args:
        username: the mysql server username
        password: the password to mysql server
        database: the database name
    '''
    # connect to mysql database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # create cursor class
    cur = db.cursor()

    # make query
    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"
    cur.execute(query, (state_name,))
    result = cur.fetchall()

    # print result
    for row in result:
        print(row)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    no_injection(username, password, database, state_name)
