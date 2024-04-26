#!/usr/bin/python3
'''
 a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported
'''
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    adds state to database
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost/{}' \
             .format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
 
    print('{0}'.format(new_state.id))
    session.close()
