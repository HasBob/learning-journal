from sqlalchemy import (
    Column,
    DateTime,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText
    )

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

import datetime

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
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    @classmethod
    def all(cls, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).order_by(sa.sec(cls.created)).all() # still needs to be updated to sort descending

    @classmethod
    def by_id(cls, id, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).get(id)

Index('entries_index', Entry.created)

#Index('my_index', MyModel.name, unique=True, mysql_length=255)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)

    @classmethod
    def by_name(cls, name, session=None):
        if session is None:
            session = DBSession
        return DBSession.query(cls).filter(cls.name == name).first()
