#!/usr/bin/python3
"""Module that prints all states by ASCENDING order"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Get MySQL username, password, and database
    name from command line arguments
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    # state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=mysql_username,
                        password=mysql_password,
                        database=database_name
                        )

    c = db.cursor()

    query = """SELECT cities.id, cities.name,
              states.name FROM cities
              JOIN states ON cities.state_id = states.id
              ORDER BY cities.id ASC"""

    c.execute(query,)

    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
