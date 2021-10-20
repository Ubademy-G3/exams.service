from sqlalchemy import (Column, Integer, String, Table, MetaData)

metadata = MetaData()

exams = Table(
    'exams',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)
