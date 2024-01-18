#!/usr/bin/python3

"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
Script must take 3 arguments: mysql username, mysql password and database name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":

    # Check if the number of arguments is correct
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    # Creating the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating the tables in the database
    Base.metadata.create_all(engine)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating the State "California" with the City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Adding the State and City objects to the session and committing changes
    session.add(new_state)
    session.add(new_city)
    session.commit()

    # Closing the session
    session.close()
