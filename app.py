
#7Hhgsq7dGfibhHLC2YNQjEK_pMK9jB5N_HDqzLCM
CLARIFAI_APP_ID ="ptutSXCUdWgBfInt4WzBbVa2RZYUTkeZ2jli4jdE"


#CLARIFAI_APP_ID=""
from flask import Flask, request, render_template
app = Flask(__name__)

from clarifai.rest import ClarifaiApp

app2 = ClarifaiApp()
app2.tag_urls(['https://samples.clarifai.com/metro-north.jpg'])

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route("/genderpage")
def selectgender():
	return "This will be the he and she page"


if __name__ == "__main__":
    app.run()