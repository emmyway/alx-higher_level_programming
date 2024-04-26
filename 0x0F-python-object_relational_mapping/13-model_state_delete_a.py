#!/usr/bin/python3
'''
 a script that deletes all State objects with a name containing
 the letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from
model_state import Base, State
Your script should connect to a MySQL server running
on localhost at port 3306
Your code should not be executed when imported
'''
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    changes state name in database
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost/{}' \
             .format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name.contains('a'))
    if state is not None:
        for state in state:
            session.delete(state)

    session.commit()
 
    session.close()
