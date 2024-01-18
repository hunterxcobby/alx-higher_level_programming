#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
Parameters for script: mysql username, mysql password, database name and
state name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `cities.id`.
Can only use `execute()` once
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

    # createing a cursor object to execute SQL queries
    cursor = db.cursor()

    # using parameters to safely execute the query and avoid SQL injection
    city_query = """SELECT cities.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.state_id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC"""
    cursor.execute(city_query, (argv[4],))

    # fetching all the results
    cities = cursor.fetchall()

    # Displaying the results in the requested format
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))
    """
    # display/print them out
    for city in cities:
        print(city)"""

    # closing the cursor and database connection
    cursor.close()
    db.close()
