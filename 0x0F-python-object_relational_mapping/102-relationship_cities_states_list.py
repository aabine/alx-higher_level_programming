#!/usr/bin/python3
""" Prints the State object with the name
passed as an argument from the database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            print(
                "Usage: {} <username> <password> <database>"
                .format(sys.argv[0]))
            sys.exit(1)

        username, password, database = sys.argv[1:4]

        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database
            )
        )
        Base.metadata.create_all(engine)

        # Use the session as a context manager to ensure it's properly closed
        with sessionmaker(bind=engine)() as session:
            # Fetch all states and cities in a single query
            states = session.query(State).order_by(State.id).all()

            for state in states:
                for city in state.cities:
                    print(city.id, city.name, sep=": ", end=" -> ")
                    print(state.name)
    except Exception as e:
        print("Error:", e)
