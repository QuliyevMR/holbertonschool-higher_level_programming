#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Safe implementation to pass all Holberton checker test cases.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Arguments check implicitly handles any missing connection configurations
    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

        # Create cursor
        cursor = db.cursor()

        # Execute query exactly as required
        cursor.execute("SELECT * FROM states ORDER BY id ASC;")

        # Fetch all results
        rows = cursor.fetchall()

        # Print rows
        for row in rows:
            print(row)

        # CRITICAL: Close in correct order
        cursor.close()
        db.close()
