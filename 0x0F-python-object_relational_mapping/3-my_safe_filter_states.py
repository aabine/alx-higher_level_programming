#!/usr/bin/python3
"""
Display all values in the states table of hbtn_0e_0_usa
where name matches the argument (safe from MySQL injection).
"""

import MySQLdb
import sys

def display_states(username: str, password: str,
                     database: str, state_name: str) -> None:
    """
    Display all values in the states table where name matches the argument.

    Args:
        username: The username for the database connection.
        password: The password for the database connection.
        database: The name of the database.
        state_name: The name of the state to search for.

    Returns:
        None
    """

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        query = """
            SELECT * FROM states
            WHERE name LIKE BINARY %s
            ORDER BY states.id
        """

        with db.cursor() as cursor:
            cursor.execute(query, (state_name,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("""Usage: {} <username> <password> <database>
             <state_name>""".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
    display_states(username, password, database, state_name)