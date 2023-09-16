#!/usr/bin/python3
"""
Print all states whose names match a provided argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        state_name = sys.argv[4]

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
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()
