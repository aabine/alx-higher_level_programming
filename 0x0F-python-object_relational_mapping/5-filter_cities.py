#!/usr/bin/python3
"""
List all cities in a state based on a given
argument from the database hbtn_0e_4_usa 
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:5]

    try:
        # Connect to the database
        dbconnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor
        with dbconnect.cursor() as cursor:
            # Use parameterized query
            query = """
                SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id
            """
            cursor.execute(query, (state_name,))

            # Fetch and print results
            rows = cursor.fetchall()
            if rows:
                result = ', '.join(row[1] for row in rows)
                print(result)
            else:
                print()
    except MySQLdb.Error as e:
        print("Database error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        # Close connection
        dbconnect.close()
