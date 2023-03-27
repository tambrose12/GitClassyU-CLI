from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Course)

if __name__ == '__main__':
    engine = create_engine('sqlite:///models.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    bio = Course("Biology", 1000, 4, "Mendel")
    his = Course("History", 1000, 3, "Aristotle")

    session.add(bio)
    session.commit()


import ipdb; ipdb.set_trace()