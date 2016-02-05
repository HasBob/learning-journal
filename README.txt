learning_journal README
==================

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/python setup.py develop

- $VENV/bin/setup_db development.ini

- $VENV/bin/pserve development.ini

'''
from sqlalchemy import engine_from_config
engine = engine_from_config(registry.settings, 'sqlalchemy.', echo=True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
from learning_journal.models import Entry
session.query(Entry).all()

q1 = session.query(Entry.id, Entry.title, Entry.body, Entry.created, Entry.edited)