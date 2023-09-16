#!/usr/bin/python3
"""
Print all states whose names match a provided argument.
"""
import MySQLdb
import sys

# Connect to the MySQL server
connection = MySQLdb.connect(host="localhost",port=3306,
                             user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

# Create a cursor object
cursor = connection.cursor()

# Execute the SQL query
query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id"
state_name = sys.argv[4]
cursor.execute(query, (state_name,))

# Fetch all the rows
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
connection.close()