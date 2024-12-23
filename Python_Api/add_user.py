from sqlalchemy import create_engine, Column, Integer, String, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_user(username, password):
    new_user = User(username=username, password=password)
    try:
        session.add(new_user)
        session.commit()
        print(f"Kullanıcı {username} eklendi.")
    except exc.IntegrityError:
        session.rollback()
        print("Bu kullanıcı adı zaten mevcut.")

add_user("admin1", "12345")
add_user("admin2", "123456")
add_user("test", "12345")
