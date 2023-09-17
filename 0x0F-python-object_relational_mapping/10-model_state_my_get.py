#!/usr/bin/python3
"""Print all states whose names match a provided argument."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>"
            .format(sys.argv[0])
        )
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    try:
        connection_string = (
            f"mysql+mysqldb://{username}:{password}@localhost/{database}"
        )

        engine = create_engine(connection_string)
        Base.metadata.create_all(engine)

        # Use a context manager for the session
        with sessionmaker(bind=engine)() as session:
            states = session.query(State).filter(
                State.name == state_name
            ).order_by(State.id).all()
            if states:
                for state in states:
                    print("{}".format(state.id))
            else:
                print("Not found")
    except Exception as e:
        print("Error:", e)
