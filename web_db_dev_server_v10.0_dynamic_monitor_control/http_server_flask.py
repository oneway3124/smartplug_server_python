from flask import Flask, request, render_template, session, jsonify, abort, make_response
import random
from dao import Dao
from model import PowerPara
import redis

r=redis.Redis(host="localhost")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

#@app.route('/<name>')
#def index(name=None):
#   return render_template('hello.html',name=name)
   
@app.route('/', methods=['GET', 'POST'])
def home():
    str = "Vol"
    li = [230,2,3,4]
    rand1=random.randint(220,250)
    rand2=random.randint(0,10)
    #print(random.randint(0,99))
    da = Dao()
    power_data = PowerPara()
    #power_data.vol = str(data)
    #power_data.cur = "123"
    #power_data.power = "22"
    str2=da.findData(power_data,2,3)
	# return db find data
    #print(str2)
    vol=random.randint(220,240)
    cur=random.randint(0,20)
    pwr=random.randint(0,2)
    tmp=random.randint(0,40)
    rssi=random.randint(0,80)
    #print(str1)
    return render_template('general_parameters.html',vol=vol,cur=cur,pwr=pwr,tmp=tmp,rssi=rssi)

	
@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

@app.route('/control', methods=['POST'])
def control():
    return render_template('control.html')

@app.route('/vol', methods=['POST'])
def vol_dis():
    print("vol page")
    name=r.lpop("vol_list")
    print(r.lpop("vol_list"))
    return render_template('vol_parameters.html',name=name)
	
@app.route('/cur', methods=['POST'])
def cur_dis():
    print("cur page")
    name=r.lpop("vol_list")
    print(r.lpop("vol_list"))
    return render_template('cur_parameters.html',name=name)	

@app.route('/pwr', methods=['POST'])
def pwr_dis():
    return render_template('pwr_parameters.html')	

@app.route('/tmp', methods=['POST'])
def tmp_dis():
    return render_template('tmp_parameters.html')	

@app.route('/rssi', methods=['POST'])
def rssi_dis():
    return render_template('rssi_parameters.html')	

parameters = [
    {
        'id': 1,
        'vol': 230,
        'cur': 2,
        'pwr': 2,
        'tmp': 20,
        'rssi': -65,
        'description': u'xxx',
        'done': False
    },
    {
        'id': 2,
        'vol': 231,
        'cur': 23,
        'pwr': 2,
        'tmp': 20,
        'rssi': -65,
        'description': u'yyyy',
        'done': False
    }
]

##RESTful API GET
@app.route('/smartplug/api/parameters', methods=['GET'])
def get_tasks():
    return jsonify({'parameters': parameters})	

##RESTful API POST	
@app.route('/smartplug/api/control', methods=['POST'])
def create_task():
    if not request.json or not 'vol' in request.json:
        abort(400)
    parameter = {
		'id': parameters[-1]['id'] + 1,
		'vol': request.json['vol'],
		'description': request.json.get('description', ""),
		'done': False
    }
    parameters.append(parameter)
	### send redis message to device server
    return jsonify({'parameter': parameter}), 201

if __name__ == '__main__':
   app.run(host="0.0.0.0")
   