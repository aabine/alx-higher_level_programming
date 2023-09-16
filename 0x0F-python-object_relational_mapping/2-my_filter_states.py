#!/usr/bin/python3
""" print all states passed as argument """
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
        with db.cursor() as cursor:
            cursor.execute("""SELECT * FROM states WHERE name
                             LIKE BINARY '{}' ORDER BY states.id""".format(sys.argv[4]))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        db.close()
