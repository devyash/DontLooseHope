
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

@app.route("/findmissingperson", methods=['GET', 'POST'])

def findmissingperson():
	if request.method == 'POST':
		updatedb(request.form['name'],request.form['email'],request.form['phonenumber'])
		url=uploadimage(image)
		errortrain=trainclari(url)
		(name,error) = check(url)
		return render_template('displayresult.html', error=error, name=name)
	else:
		return render_template('findmissingperson.html')


@app.route("/reportmissingperson")
def reportmissingperson():
	if request.method == 'POST':
		#check(url)
		print("Reached here")
		return "Good Work"
		#render_template('displayresult.html'"")
	else:
		return render_template('reportmissingperson.html')


##Various function defined above

def trainclari(url,name):
	#This function would train the clarifau 
	#errortrain=true if not done
	#errortrain=false if response =ok
	return errortrain




def check(url):
	#this function would call predict on the submited image and 
	# if the value is greater than 0.75
	# it would return error as false
	return (name,error)

def uploadimage():
	# This function would upload a image to imgur and return the url
	return none

def updatedb(name,email,phonenumber):
	#this function is sqlalchemy commands to update the database
	return none
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)