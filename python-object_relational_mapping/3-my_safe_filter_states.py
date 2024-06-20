#!/usr/bin/python3
"""Module that prints all states by ASCENDING order"""
import MySQLdb
import sys
import mysql.connector

if __name__ == "__main__":
    """
    Get MySQL username, password, and database
    name from command line arguments
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=mysql_username,
                        password=mysql_password,
                        database=database_name
                        )

    c = db.cursor()

    query = """SELECT * FROM states WHERE name = %s ORDER BY id ASC"""
    c.execute(query, (state_name_searched,))

    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
