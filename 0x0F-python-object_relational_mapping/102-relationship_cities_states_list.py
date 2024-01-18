#!/usr/bin/python3

"""
Script that lists all City objects from the database hbtn_0e_101_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
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

    # Querying all City objects with their corresponding State objects
    # using the state relationship
    cities = session.query(City).order_by(City.id).all()

    # Displaying the results
    for city in cities:
        state_name = city.state.name if city.state else "None"
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    # Closing the session
    session.close()
