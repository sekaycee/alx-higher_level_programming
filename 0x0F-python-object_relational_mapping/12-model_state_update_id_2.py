#!/usr/bin/python3
''' Change the name of a State object from the database hbtn_0e_6_usa '''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    edit_state = session.query(State).filter(State.id == 2).first()
    edit_state.name = 'New Mexico' if edit_state
    session.commit()
    session.close()
