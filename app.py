from flask import Flask, redirect, url_for, request
from datetime import datetime
import custom.powershell as powershell
import custom.PyWin as pywin
import json

# Initialize JSON Data
data = open('settings.json')
jsonData = json.load(data)

# Make the flask class
app = Flask(__name__, static_folder='static')

# Home page rendering
@app.route('/')
def index():
	return app.send_static_file('index.html')
	
# Get JSON Data [CALLED FROM JS]
@app.route('/getjson/', methods=['POST'])
def getjson():
	# We're using globals here so don't forget those
	global data
	global jsonData

	# Refresh JSON Data [Using the globals declared above]
	data = open('settings.json')
	jsonData = json.load(data)
	return jsonData


@app.route('/run/button/', methods=['POST'])
def test():
	# Declare shit
	index = request.json["index"]
	buttonAction = jsonData['grid'][index]['action']

	# Print pushed button action for debugging purposes
	print(jsonData['grid'][index]['index'] + ": [" + jsonData['grid'][index]['action'] + "]")

	if (buttonAction == "mute"):
		powershell.run("$(new-object -com wscript.shell).SendKeys([char]173)")
	elif (buttonAction == "mute-mic"):
		pywin.mute()

	# Return shit
	return ''


# Actually run it
if __name__ == '__main__':
	app.run(debug=True, port=80, host='0.0.0.0')
