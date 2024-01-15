#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # establishing a secure connection to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # executing the cursor to retrieve states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetching all the results
    states = cursor.fetchall()

    # display/print them out
    for state in states:
        print(state)

    # closing the cursor and database connection
    cursor.close()
    db.close()
