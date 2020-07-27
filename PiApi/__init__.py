from flask import Flask, jsonify, request
import RPi.GPIO as GPIO


#getting current user
#import getpass
#getpass.getuser()

#utilities functions
def boardsetup(mode):
	if mode=='bcm' or mode=='BCM':
		GPIO.setmode(GPIO.BCM)
	elif mode=='board' or mode=='BOARD':
		GPIO.setmode(GPIO.BOARD)
	else:
		return jsonify({'status':0,'msg':'mode can be board or bcm'})
	return {'status':1,'msg':'pi has been setup in {} mode'.format(mode)}


def isGPIO(pin):
	return pin in gpios

# def getpinmode(pin):
# 	return 

#end of utility functions


app = Flask(__name__)


gpios = [11,13,15,16,18,22,36,38,40]

boardsetup('BOARD')		#Use default board pin numbering, can be Set in BCM Mode    



@app.route('/')
def greet():
	return jsonify({'greet':'Welcome to respberrypi flask api'})

@app.route('/pinsetup', methods=['GET'])
def pinsetup():
	pin = int(request.args['pin'])
	if not isGPIO(pin):
		return jsonify({'status':0,'msg':'pin must be a gpio pin.'})
	mode = request.args['mode']
	if mode=='in' or mode=='IN':
		GPIO.setup(pin,GPIO.IN)
	elif mode=='out' or mode=='OUT':
		GPIO.setup(pin,GPIO.OUT)
	else:
		return jsonify({'status':0,'msg':'possible values of mode are in,IN,out,OUT'})
	return jsonify({'status':1,'msg':'Success'})


@app.route('/getvalue', methods=['GET'])
def getvalue():
	pin = int(request.args['pin'])
	if not isGPIO(pin):
		return jsonify({'status':0,'msg':'pin must be a gpio pin'})
	state = GPIO.input(pin)
	return jsonify({'status':1,'state':state})


@app.route('/setoutput', methods=['GET'])
def setoutput():
	pin = int(request.args['pin'])
	if not isGPIO(pin):
		return jsonify({'status':0,'msg':'pin must be a gpio pin'})
	value = int(request.args['value'])
	try:
		GPIO.output(pin,value)
	except RuntimeError as e:
		return jsonify({'status':0,'msg':str(e)})
	return jsonify({'status':1,'msg':'Success'})


@app.route('/setinput', methods=['GET'])
def setinput():
	pin = int(request.args['pin'])
	if not isGPIO(pin):
		return jsonify({'status':0,'msg':'pin must be a gpio pin'})
	value = int(request.args['value'])
	GPIO.input(pin,value)
	return jsonify({'status':1,'msg':'Success'})

@app.route('/getgpios', methods=['GET'])
def getgpios():
	return jsonify({'status':1,'pins':gpios})