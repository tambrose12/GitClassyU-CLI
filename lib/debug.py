from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from seed import seed
from db import *

from db.models import (Base, Course)
seed()

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///models.db')
#     # Base.metadata.create_all(engine)

#     Session = sessionmaker(bind=engine)
#     session = Session()

#     bio = Course(name="Biology", level=1000, credits=4)
#     his = Course(name="History", level=1000, credits=3)

#     session.add(bio)
#     session.commit()

#     session.add(his)
#     session.commit()

import ipdb
ipdb.set_trace()
