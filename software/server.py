from flask import Flask
from moduleImgToText.connector import getText
from library import speak
from moduleImageCaptioning.script import getCaption
from moduleFaceRecon.connector import recognise
app = Flask(__name__)

# command L1
@app.route('/')
def home():
	context = {
		"Project": "THIRD EYE",
		"Team": "Prince Mishra(19104071), Nishant(19104059), Parth Saraswat(19104065)",
		"Mentor": "Dr. Manjeet Singh"
	}
	return context

# command L2
@app.route('/getImageText')
def getImageText():
	print("---------------Image to Text------------------")
	text = getText()
	context = {
		"status": "success",
		"text": text
	}
	# speak(text)
	return context

# command L3
@app.route('/getImageCaption')
def getImageCaption():
	print("---------------Image Caption------------------")
	text = getCaption()
	context = {
		"status": "success",
		"text": text
	}
	# speak(text)
	return context

# command L4
@app.route('/recognisePerson')
def recognisePerson():
	print("---------------Face Recognise------------------")
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
