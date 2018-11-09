from flask import Flask, request, render_template, session, jsonify, abort, make_response
import random
from dao import Dao
from model import PowerPara
import redis
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

r=redis.Redis(host="localhost")

app = Flask(__name__)
api = Api(app)
CORS(app, resources=r'/*')

app.config['SECRET_KEY'] = 'hard to guess string'

#@app.route('/<name>')
#def index(name=None):
#   return render_template('hello.html',name=name)

@app.route('/baidu.html', methods=['GET'])
def baidu():
    return render_template('baidu.html')

@app.route('/index.html', methods=['GET', 'POST'])
def index():
    #Address = request.form['address']
    Address = request.args["address"]
    #return render_template('index.html')	
    return render_template('index.html',Address=Address)	
   
@app.route('/detail.html', methods=['GET'])
def detail():
    type = request.args["type"]
    deviceId = request.args["deviceId"]
    return render_template('detail.html',type=type,deviceId=deviceId)
	
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
    #push data into redis
    print(r.rpush("action","off"))
    return render_template('control.html')

@app.route('/vol', methods=['POST'])
def vol_dis():
    print("vol page")
	#b"b'vol:0231  \\x00'"
    name=r.lpop("vol_list")
    print(name)
    name = name[6:10]
    print(name)
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
        'dev_id': 1,
        'id':1,
        'vol': 220,
        'cur': 21,
        'pwr': 22,
        'tmp': 20,
        'rssi': -65,
        'description': u'xxx',
        'action': 1
    },
	{
        'dev_id': 1,
        'id':2,
        'vol': 221,
        'cur': 1,
        'pwr': 2,
        'tmp': 20,
        'rssi': -65,
        'description': u'xxx',
        'action': 1
    },
	{
        'dev_id': 1,
        'id':3,
        'vol': 223,
        'cur': 2,
        'pwr': 2,
        'tmp': 20,
        'rssi': -65,
        'description': u'xxx',
        'action': 1
    },
	{
        'dev_id': 1,
        'id':4,
        'vol': 224,
        'cur': 2,
        'pwr': 2,
        'tmp': 20,
        'rssi': -65,
        'description': u'xxx',
        'action': 1
    },
    {
        'dev_id': 1,
		'id':5,
        'vol': 225,
        'cur': 23,
        'pwr': 2,
        'tmp': 20,
        'rssi': -65,
        'description': u'yyyy',
        'action': 1
    }
]

##RESTful API GET
@app.route('/smartplug/api/parameters', methods=['GET'])
def get_tasks():
    return jsonify({'parameters': parameters})	

##RESTful API POST	
'''
@app.route('/smartplug/devices/control', methods=['POST'])
def create_task():
    if not request.json or not 'action' in request.json:
        abort(400)
    parameter = {
		'dev_id':1,
		'id': parameters[-1]['id'] + 1,
		#'vol': request.json['vol'],
		'action': request.json['action'],
		'description': request.json.get('description', "")
    }
    parameters.append(parameter)
	### send redis message to device server
    return jsonify({'parameter': parameter}), 201
'''

device_stat={
        'error':'succ',
		'data':
		[
			{
				'address':'jijiaolou',
				'num':'5',
				'location':{'lon':'104.087556','lat':'30.637192'}
			},
			{
				'address':'yjsyuan',
				'num':'6',
				'location':{'lon':'104.086649','lat':'30.635818'}
			}
		]
}

#@app.route('/smartplug/devices_num', methods=['GET'])
#def get_devices_num():
#    return jsonify(device_stat)

	
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
		
class devices_num(Resource):
    def get(self):
        return device_stat

devices_info={
	'error':'succ',
	'data':
	[
		{
			'dev_id':'12345',
			'desc':'wangwei',
			'online':'true',
			'address':'jijiaolou',
			'location':{'lon':'104.087556','lat':'30.637192'},
			'owner_info':'wsn'
		},
		{
			'dev_id':'12346',
			'desc':'wangwei',
			'online':'true',
			'address':'jijiaolou',
			'location':{'lon':'104.087556','lat':'30.637192'},
			'owner_info':'wsn'
		}
	]
}	

class devices(Resource):
    def get(self):
        return devices_info	

device_single={
	'error':'succ',
	'data':
	{
			'dev_id':'12345',
			'desc':'wangwei',
			'online':'true',
			'address':'jijiaolou',
			'location':{'lon':'104.087556','lat':'30.637192'},
			'vol':'230',
			'cur':'2',
			'pwr':'10',
			'tmp':'25',
			'rssi':'-65',
			'action':'on',
			'owner_info':'wsn'
	}
}	
class device_id(Resource):
    def get(self,dev_id):
        return device_single



vol_info={
	'error':'0',
	'data':
	{
		'dev_id':'12345',
		'desc':'wangwei',
		'online':'true',
		'location':{'lon':'104.087556','lat':'30.637192'},
		'vol':['230','231','227','220','228','235','220','225','220','221'],
		'owner_info':'wsn'
	}
}
'''
        name=r.lpop("vol_list")
        print(name)
        name = name[6:10]
        print(name) 
        name = str(name,encoding="utf-8")
        print(name)
		'''	
class vol_lastest_info(Resource):
    def get(self,dev_id):
        vol_lastest=[]
        #vol_lastest.append(name)
        for i in range(10):
            name=r.lpop("vol_list")
            name = name[4:8]
            name = str(name,encoding="utf-8")
            vol_lastest.append(name)
        print(vol_lastest)
		
        vol_info={
			'error':'0',
			'data':
            {
			    'dev_id':'12345',
			    'desc':'wangwei',
			    'online':'true',
			    'location':{'lon':'104.087556','lat':'30.637192'},
			    'vol':vol_lastest,
			    'owner_info':'wsn'
            }
        }
        return vol_info

cur_info={
	'error':'0',
	'data':
	{
		'dev_id':'12345',
		'desc':'wangwei',
		'online':'true',
		'location':{'lon':'104.087556','lat':'30.637192'},
		'cur':['20','21','12','2','34','5','26','7','38','29'],
		'owner_info':'wsn'
	}
}
	
class cur_lastest_info(Resource):
    def get(self,dev_id):
        return cur_info

pwr_info={
	'error':'0',
	'data':
	{
		'dev_id':'12345',
		'desc':'wangwei',
		'online':'true',
		'location':{'lon':'104.087556','lat':'30.637192'},
		'pwr':['20','21','12','2','34','5','26','7','38','29'],
		'owner_info':'wsn'
	}
}
	
class pwr_lastest_info(Resource):
    def get(self,dev_id):
        return pwr_info
		
tmp_info={
	'error':'0',
	'data':
	{
		'dev_id':'12345',
		'desc':'wangwei',
		'online':'true',
		'location':{'lon':'104.087556','lat':'30.637192'},
		'tmp':['20','21','12','2','34','5','26','7','38','29'],
		'owner_info':'wsn'
	}
}
	
class tmp_lastest_info(Resource):
    def get(self,dev_id):
        return tmp_info

rssi_info={
	'error':'0',
	'data':
	{
		'dev_id':'12345',
		'desc':'wangwei',
		'online':'true',
		'location':{'lon':'104.087556','lat':'30.637192'},
		'tmp':['20','21','12','2','34','5','26','7','38','29'],
		'owner_info':'wsn'
	}
}
	
class rssi_lastest_info(Resource):
    def get(self,dev_id):
        return rssi_info
		
control_response={
	'error':'succ'
}	
	
class device_control(Resource):
    def get(self):
        return control_response
		
    def post(self):
        
        args = parser.parse_args()
       
        #push data into redis
        #if var%2==0:
        #print('------')
        print(r.rpush("action","on"))
        #elif var%2==1:
        #print('+++++++')
        #print(r.rpush("action","off"))
        return control_response,201
##
## Actually setup the Api resource routing here
##
api.add_resource(devices_num,'/smartplug/devices_num')
api.add_resource(devices,'/smartplug/devices')
api.add_resource(device_id,'/smartplug/devices/<dev_id>')
api.add_resource(vol_lastest_info,'/smartplug/devices/vol_lastest_info/<dev_id>')
api.add_resource(cur_lastest_info,'/smartplug/devices/cur_lastest_info/<dev_id>')
api.add_resource(pwr_lastest_info,'/smartplug/devices/pwr_lastest_info/<dev_id>')
api.add_resource(tmp_lastest_info,'/smartplug/devices/tmp_lastest_info/<dev_id>')
api.add_resource(rssi_lastest_info,'/smartplug/devices/rssi_lastest_info/<dev_id>')
api.add_resource(device_control,'/smartplug/device/control')
	
if __name__ == '__main__':
   app.run(host="0.0.0.0")
   