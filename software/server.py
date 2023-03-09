from flask import Flask
from moduleImgToText.connector import getText
from library import speak

app = Flask(__name__)

@app.route('/')
def hello_world():
	context = {
		"name": "Prince Mishra",
		"course": "B.Tech"
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

# main driver function
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
