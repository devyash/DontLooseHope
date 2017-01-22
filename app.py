
from flask import Flask, request, render_template
app = Flask(__name__)

from clarifai.rest import ClarifaiApp
import os,sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from dB_setup import Base, MissingPeople,FoundPeople
from clarifai.rest import Image as ClImage
import json
import time


# Connect to Database and create database session
engine = create_engine('sqlite:///DLH.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app2 = ClarifaiApp()
model = app2.models.get('dontloosehope')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route("/findmissingperson", methods=['GET', 'POST'])
def findmissingperson():
	if request.method == 'POST':

		updatedb(request.form['name'],request.form['email'],request.form['phonenumber'])
		(searchname,error) = check(request.form['imageurl'])

		if(error!=True):
			(name,address,phonenumber,email)=querydb(searchname)
			trainclari(request.form['imageurl'],request.form['name'])
	

			return render_template('displaytrueresult.html', searchname=searchname, name= name,address=address,phonenumber=phonenumber,email=email)
		else:
			trainclari(request.form['imageurl'],request.form['name'])

			return render_template('displayfalseresult.html', searchname=searchname)
		# return "Hello World!"
	else:
		return render_template('findmissingperson.html')




# @app.route("/reportmissingperson")
# def reportmissingperson():
# 	if request.method == 'POST':
# 		#check(url)
# 		print("Reached here")
# 		return "Good Work"
# 		#render_template('displayresult.html'"")
# 	else:
# 		return render_template('reportmissingperson.html')


##Various function defined above

def trainclari(url,name):
	#This function would train the clarifau 
	#errortrain=true if not done
	#errortrain=false if response =ok

	app2.inputs.create_image_from_url(url=url, concepts=[name])
	return 0




def check(url):
#this function would call predict on the submited image and 
# if the value is greater than 0.75
# it would return error as false
	# image = ClImage(url=url)
	print (url)
	parsed_input = model.predict_by_url(url)
	print(parsed_input)
	if ((parsed_input['status'])['code'] != 10000):
		print('Status:', response.status_code, 'Problem with the request. Exiting.')
		return (0,0)
	
	concepts = parsed_input['outputs'][0]['data']['concepts']
	max=0
	name=0
	error=True
	for concept in concepts:
		if (concept['value']>=0.85 and concept['value']>max):
			max=concept['value']
			name=max['name']
			error = False   
	return (name,error)



def updatedb(name,email,phonenumber):
	#this function is sqlalchemy commands to update the database
	newMissingPeople=MissingPeople(email=email,phonenumber=phonenumber,name=name)
	session.add(newMissingPeople)
	session.commit()
	return 0

def querydb(searchname):
	#this function queries the Found People Db and return the above 
	#details of the person if the person is found 
	foundperson = session.query(FoundPeople).filter_by(name = searchname).one()
	return (foundperson.email,foundperson.phonenumber,foundperson.address,foundperson.name)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)