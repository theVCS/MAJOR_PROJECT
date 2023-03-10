from flask import Flask
from moduleImgToText.connector import getText
from library import speak
from moduleImageCaptioning.script import getCaption
from moduleFaceRecon.connector import recognise
app = Flask(__name__)

@app.route('/')
def home():
	context = {
		"Project": "THIRD EYE",
		"Team": "Prince Mishra(19104071), Nishant(19104059), Parth Saraswat(19104065)",
		"Mentor": "Dr. Manjeet Singh"
	}
	return context

@app.route('/getImageText')
def getImageText():
	text = getText()
	context = {
		"status": "success",
		"text": text
	}
	# speak(text)
	return context

@app.route('/getImageCaption')
def getImageCaption():
	text = getCaption()
	context = {
		"status": "success",
		"text": text
	}
	# speak(text)
	return context


@app.route('/recognisePerson')
def recognisePerson():
	text = recognise()
	context = {
		"status": "success",
		"text": text
	}
	# speak(text)
	return context


# main driver function
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
