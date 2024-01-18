#!/usr/bin/python3

"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `SQLAlchemy` module.
Must import `State` and `Base` from `model_state` -
`from model_state import Base, State`
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Print the new states.id after creation.
Code should not be executed when imported.
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Check if the number of arguments is correct
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    # Creating the connection string (engine for database)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # creating a new State Object
    new_state = State(name="Louisiana")

    # Adding the State Object to the session and committing the changes
    session.add(new_state)
    session.commit()

    # displaying the new state's id
    print("{}".format(new_state.id))

    # Closing the session
    session.close()
