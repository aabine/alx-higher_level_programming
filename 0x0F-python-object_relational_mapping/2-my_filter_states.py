#!/usr/bin/python3
""" Print all states whose names match a provided argument. """
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    state_name = sys.argv[4]
    cursor = connection.cursor()
    cursor.execute(
        """SELECT * FROM states
           WHERE name LIKE BINARY '{}'
           ORDER BY states.id""".format(state_name)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
