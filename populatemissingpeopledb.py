import os,sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from dB_setup import Base, MissingPeople,FoundPeople

# Connect to Database and create database session
engine = create_engine('sqlite:///DLH.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



devyash=MissingPeople(email="prince@clarifai.com",phonenumber=3522845228,name="Devyash Sanghai")
tanu=MissingPeople(email="devbackhome@gmail.com",phonenumber=3522262431,name="Vaibhav Somani")
vaibhav=MissingPeople(email="R@gmail.com",phonenumber=3522262431,name="Tanu Gupta")
prithvi=MissingPeople(email="S@gmail.com",phonenumber=3522262431,name="Prithvi Monagi")

session.add(prithvi)
session.add(vaibhav)
session.add(devyash)
session.add(tanu)
session.commit()