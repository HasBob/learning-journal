from sqlalchemy import (
    Column,
    DateTime,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

import datetime

def now():
    return datetime.datetime.now()

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


#class MyModel(Base):
#    __tablename__ = 'models'
#    id = Column(Integer, primary_key=True)
#    name = Column(Text)
#    value = Column(Integer)

# http://docs.sqlalchemy.org/en/rel_0_9/core/metadata.html#sqlalchemy.schema.Column

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False) # maybe? types.Unicode ?
    body = Column(UnicodeText)
    created = Column(DateTime, default=now) #DateTime? 
    edited = Column(DateTime, default=now, onupdate=now)

    @classmethod
    def all(cls, session=None):
        if session == None:
            session = DBSession
        return session.query(cls).order_by(cls.created).all()

    @classmethod
    def by_id(cls, id, session=None):
        if session == None:
            session = DBSession
        return session.query(cls).get(id)

Index('entries_index', Entry.created)

#Index('my_index', MyModel.name, unique=True, mysql_length=255)
