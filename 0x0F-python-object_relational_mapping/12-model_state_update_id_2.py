#!/usr/bin/python3
""" Update a State object from the database hbtn_0e_6_usa """
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
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, database)
        )
        Base.metadata.create_all(engine)
        with sessionmaker(bind=engine)() as session:
            new_state = State(id=2, name="New Mexico")
            session.add(new_state)
            session.commit()
            state = session.query(State).order_by(State.id.desc()).first()
            print("{}".format(state.id))
    except Exception as e:
        print("Error:", e)
