#!/usr/bin/python3
'''
a script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username, mysql
password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported
'''
import MySQLdb
import sys


def all_cities(username, password, database):
    '''
    script prints all cities in states
    Args:
        username: the mysql server username
        password: the password to mysql server
        database: the database name
    '''
    # connect to server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    # create a cursor object
    cur = db.cursor()
    # make a query
    query = "SELECT * FROM cities ORDER BY id ASC"
    cur.execute(query)
    # print result
    result = cur.fetchall()
    for row in result:
        print(row)
    # clean up
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # call function
    all_cities(username, password, database)
