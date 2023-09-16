#!/usr/bin/python3
""" print the first State object """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    try:
        connection = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, database)
        )
        Session = sessionmaker(bind=connection)
        session = Session()
        state = session.query(State).order_by(State.id).first()
        if state:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")
        session.close()
    except Exception as e:
        print("Error:", e)
