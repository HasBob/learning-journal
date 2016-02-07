learning_journal README
==================

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/python setup.py develop

- $VENV/bin/setup_db development.ini

- $VENV/bin/pserve development.ini

'''
pshell development.ini

from sqlalchemy import engine_from_config
engine = engine_from_config(registry.settings, 'sqlalchemy.', echo=True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
from learning_journal.models import Entry
session.query(Entry).all()

q1 = session.query(Entry.id, Entry.title, Entry.body, Entry.created, Entry.edited)

def printshit(q):
for a,b,c,d,e in q:
    print(a,b,c,d,e)
    print(type(a),type(b),type(c),type(d),type(e))

some bodies to add to the db:
b2 = Entry(title='judgement day', body='hasta la vista')
b3 = Entry(title='three amigos', body = 'plethora of piñatas')