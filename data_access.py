from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base
from sqlalchemy import create_engine,Column,and_, or_


username = "root"
password = "r33115910"
database_name = "online_shop"

connection_string = f"mysql+pymysql://{username}:{password}@localhost:3306/{database_name}"

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class DataAccess:
    def __init__(self, class_name):
        self.class_name = class_name
        Base.metadata.create_all(bind=engine)

    def save(self, entity):
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def edit(self, entity):
        session.merge(entity)
        session.commit()
        return entity

    def remove(self, entity):
        session.delete(entity)
        session.commit()
        return entity

    def find_all(self):
        entity_list = session.query(self.class_name).all()
        if entity_list:
            return entity_list
        else:
            raise ValueError("No records found!")

    def find_by_id(self, id):
        entity = session.get(self.class_name, id)
        if entity:
            return entity
        else:
            raise ValueError("No match with this id!")
    def find_by(self, find_statement):
        entity = session.query(self.class_name).filter(find_statement).all()
        if entity:
            return entity
        else:
            raise ValueError("No match with your search!")