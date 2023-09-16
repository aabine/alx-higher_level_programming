#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    # Construct the connection string with line breaks for improved readability
    connection_string = (
        "mysql+mysqldb://{}:{}@localhost/{}?"
    ).format(username, password, database)

    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)

    # Use a context manager for the session
    with sessionmaker(bind=engine)() as session:
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
