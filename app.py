
#7Hhgsq7dGfibhHLC2YNQjEK_pMK9jB5N_HDqzLCM
CLARIFAI_APP_ID ="ptutSXCUdWgBfInt4WzBbVa2RZYUTkeZ2jli4jdE"


#CLARIFAI_APP_ID=""
from flask import Flask, request, render_template
app = Flask(__name__)

from clarifai.rest import ClarifaiApp
import os,sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from dB_setup import Base, MissingPeople,FoundPeople

# Connect to Database and create database session
engine = create_engine('sqlite:///DLH.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app2 = ClarifaiApp()
app2.tag_urls(['https://samples.clarifai.com/metro-north.jpg'])

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route("/findmissingperson")
def findmissingperson():
	return render_template('findmissingperson.html')


if __name__ == "__main__":
    app.run()