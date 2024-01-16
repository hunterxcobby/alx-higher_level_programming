#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `cities.id`.
Can only use `execute()` once
Code should not be executed when imported.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
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

    # executing the cursor to retrieve cities sorted by id
    city_query = """SELECT cities.id, cities.name, states.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.state_id
                    ORDER BY cities.id ASC"""
    cursor.execute(city_query)

    # fetching all the results
    cities = cursor.fetchall()

    # display/print them out
    for city in cities:
        print(city)

    # closing the cursor and database connection
    cursor.close()
    db.close()
