#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # create cursor
    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close cursor and db
    cursor.close()
    db.close()
