from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import (Base)

if __name__ == '__main__':
    engine = create_engine('sqlite:///models.db')
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    # CLI(user_input)



meowmeow = "lol check it out we are wizards now"

while meowmeow != 'x':
    meowmeow = input('🔥')
    if meowmeow == 'l':
        print('we love python 🐍')
    elif meowmeow != 'x':
        print(f"{meowmeow} is not the exit")
