""" script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa 
"""

import MySQLdb

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="hbtn_0e_0_usa")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except MySQLdb.Error as e:
        print("An error occurred while connecting to the database:", e)
