#!/usr/bin/python3
import MySQLdb
import sys
"""Module that prints all states by ASCENDING order"""

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=mysql_username,
                        password=mysql_password,
                        database=database_name
                        )

    # Create a cursor object to interact with the database
    c = db.cursor()
    # Execute the SQL query to select all states and order them by name in ascending order
    c.execute("""SELECT * from states ORDER BY name ASC""")

    # Fetch all the results of the query
    rows = c.fetchall()

    # Print each row in the result set
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    c.close()
    db.close()
