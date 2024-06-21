#!/usr/bin/python3
"""Module that lists all State objects from the database hbtn_0e_6_usa"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """
    Fetch all states from the database hbtn_0e_6_usa
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(mysql_username,
                                   mysql_password,
                                   database_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker()(bind=engine)

    state = session.query(State).order_by(State.id).all()

    for state in state:
        if "a" in state.name:
            session.delete(state)

    session.commit()
    session.close()
