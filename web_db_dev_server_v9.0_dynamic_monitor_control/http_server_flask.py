from flask import Flask, request, render_template
import random
from dao import Dao
from model import PowerPara

app = Flask(__name__)


#@app.route('/<name>')
#def index(name=None):
#   return render_template('hello.html',name=name)
   
@app.route('/', methods=['GET', 'POST'])
def home():
    str = "Vol"
    li = [230,2,3,4]
    rand1=random.randint(220,250)
    rand2=random.randint(0,10)
    print(random.randint(0,99))
    da = Dao()
    power_data = PowerPara()
    #power_data.vol = str(data)
    #power_data.cur = "123"
    #power_data.power = "22"
    str2=da.findData(power_data,2,3)
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
    return render_template('vol_parameters.html')
	
@app.route('/cur', methods=['POST'])
def cur_dis():
    return render_template('cur_parameters.html')	

@app.route('/pwr', methods=['POST'])
def pwr_dis():
    return render_template('pwr_parameters.html')	

@app.route('/tmp', methods=['POST'])
def tmp_dis():
    return render_template('tmp_parameters.html')	

@app.route('/rssi', methods=['POST'])
def rssi_dis():
    return render_template('rssi_parameters.html')	
	
if __name__ == '__main__':
   app.run(host="0.0.0.0")
   