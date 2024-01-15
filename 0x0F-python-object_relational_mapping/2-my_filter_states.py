#!/usr/bin/python3

"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument.
Parameters for script: mysql username, mysql password, database name
and state name searched.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Must use `format` to create the SQL query with the user input.
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # add check to see if number of arguments is correct
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit()

    # establishing a secure connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # using format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            argv[4])
    cursor.execute(query)

    # fetching all the results
    states = cursor.fetchall()

    # display/print them out
    for state in states:
        if state[1] == argv[4]:
            print(state)

    # closing the cursor and database connection
    cursor.close()
    db.close()
