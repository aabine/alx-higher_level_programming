#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""
import MySQLdb

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except MySQLdb.Error as e:
        print("An error occurred while connecting to the database:", e)
