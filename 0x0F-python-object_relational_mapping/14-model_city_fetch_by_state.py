#!/usr/bin/python3

"""
Script that prints all City objects from the database hbtn_0e_14_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `SQLAlchemy` module.
Must import `State` and `Base` from `model_state` -
`from model_state import Base, State`
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be sorted in ascending order by `cities.id`
Results must be display as they are in the example below -
(<state name>: (<city id>) <city name>)
Code should not be executed when imported.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    # Creating the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying multiple tables in database and printing info from tables
    cities = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id)

    # Displaying the results
    for city in cities:
        print("{:s}: ({:d}) {:s}".format(city[0], city[1], city[2]))

    # Closing the session
    session.close()
