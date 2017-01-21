
from flask import Flask, request, render_template
app = Flask(__name__)

from clarifai.rest import ClarifaiApp
import os,sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from dB_setup import Base, MissingPeople,FoundPeople
from clarifai.rest import Image as ClImage
import json

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
		trainclari(request.form['imageurl'],request.form['name'])
		(name,error) = check(request.form['imageurl'])
		#return render_template('displayresult.html', error=error, name=name)
		return "Hello World"
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
	image = ClImage(url)
	response = model.predict([image])
	print(response)
	# parsed_input = json.loads(response)
	# print(parsed_input)
	# if ((parsed_input['status'])['code'] != 10000):
	# 	print('Status:', response.status_code, 'Problem with the request. Exiting.')
	# exit()
	
	# concepts = parsed_input['outputs'][0]['data']['concepts']
	# for concept in concepts:
	# 	if (concept['value']>=0.85):
	# 		name = concept['name']
	# 		break
	# 	if name!=None:
	# 		error = false
	# 	else:
	# 		error = true    
	# 	return (name,error)
	return (0,0)


def updatedb(name,email,phonenumber):
	#this function is sqlalchemy commands to update the database
	newMissingPeople=MissingPeople(email=email,name=email,phonenumber=phonenumber)
	session.add(newMissingPeople)
	session.commit()
	return 0
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)