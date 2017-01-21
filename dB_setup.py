import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Boolean, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class MissingPeople(Base):
	__tablename__='missingpeople'
	id=Column(Integer,primary_key=True)
	email=Column(String(80),nullable=False)
	name=Column(String(80),nullable=False)
	phonenumber=Column(Integer,nullable=False)

class FoundPeople(Base):
	__tablename__='foundpeople'
	id=Column(Integer,primary_key=True)
	email=Column(String(80),nullable=False)
	name=Column(String(80),nullable=False)
	phonenumber=Column(Integer,nullable=False)


engine=create_engine('sqlite:///DLH.db')
Base.metadata.create_all(engine)