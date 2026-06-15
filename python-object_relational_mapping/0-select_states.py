#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    # Selecting all columns from states table, ordered by id ascending
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Clean up: close cursor and database connection
    cursor.close()
    db.close()
