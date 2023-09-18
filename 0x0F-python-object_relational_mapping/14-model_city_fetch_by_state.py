#!/usr/bin/python3
""" List all cities from the database hbtn_0e_4_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            print("Usage: {} <username> <password> <database>"
                  .format(sys.argv[0]))
            sys.exit(1)

        username, password, database = sys.argv[1:4]

        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database)
        )
        Base.metadata.create_all(engine)

        with sessionmaker(bind=engine)() as session:
            query = session.query(State, City).join(
                City, State.id == City.state_id).order_by(City.id)
            results = query.all()

            for state, city in results:
                print("{}: ({}) {}".format(state.name, city.id, city.name))
    except Exception as e:
        print("Error:", e)
