#!/usr/bin/python3
"""Script to list all State objects from a database given"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            print("Usage: {} <username> <password> <database>"
                  .format(sys.argv[0]))
            sys.exit(1)

        username, password, database = sys.argv[1:4]

        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, database),
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        with Session() as session:
            new_state = State(name="California")
            new_city = City(name="San Francisco")
            new_state.cities.append(new_city)
            session.add(new_state)
            session.add(new_city)
            session.commit()
    except Exception as e:
        print("Error:", e)
