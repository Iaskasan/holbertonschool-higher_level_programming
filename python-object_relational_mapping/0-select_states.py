#!/usr/bin/python3
import MySQLdb
import sys
"""Module that prints all states by ASCENDING order"""

if __name__ == "__main__":
    """
    Get MySQL username, password, and database
    name from command line arguments
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=mysql_username,
                        password=mysql_password,
                        database=database_name
                        )

    c = db.cursor()
    c.execute("""SELECT * from states ORDER BY name ASC""")

    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
