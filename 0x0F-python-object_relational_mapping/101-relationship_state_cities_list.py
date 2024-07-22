#!/usr/bin/env python3
'''
a script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL
server running on localhost at port 3306
You must use the cities relationship for all State objects
Your code should not be executed when imported
'''
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == "__main__":
    """
    retrieves all cities from database
    """

    db_url = "mysql+mysqldb://{}:{}@localhost/{}' \
    .format(sys.argv[1], sys.argv[2], \
            sys.argv[3]), pool_pre_ping=True"

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    
    session.commit()
    
    session.close()
