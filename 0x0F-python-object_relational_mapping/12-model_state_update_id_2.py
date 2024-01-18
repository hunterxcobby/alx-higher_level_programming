#!/usr/bin/python3

"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `SQLAlchemy` module.
Must import `State` and `Base` from `model_state` -
`from model_state import Base, State`
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Change the name of the `State` where `id = 2` to `New Mexico`
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

    # Querying the State Object where id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Checking to make sure state exists before updating it
    if state_to_update:
        # change name of the State to "New Mexico"
        state_to_update.name = "New Mexico"
        # commit changes
        session.commit()
    else:
        print("Not found")

    # Closing the session
    session.close()
