#!/usr/bin/python3
""" Delete any state with letter a from the database hbtn_0e_6_usa """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            print(
                "Usage: {} <username> <password> <database>"
                .format(sys.argv[0])
            )
            sys.exit(1)

        username, password, database = sys.argv[1:4]

        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database)
            )

        Base.metadata.create_all(engine)
        with sessionmaker(bind=engine)() as session:
            session.query(State).filter(State.name.like('%a%')).delete()
            session.commit()
    except Exception as e:
        print("Error:", e)
