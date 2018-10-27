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
    rand1=random.randint(0,300)
    rand2=random.randint(0,10)
    print(random.randint(0,99))
    da = Dao()
    power_data = PowerPara()
    #power_data.vol = str(data)
    #power_data.cur = "123"
    #power_data.power = "22"
    str2=da.findData(power_data,2,3)
    #print(str1)
    return render_template('my_template.html',str=str,li=li,str1=rand1,str2=rand2)
	
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

if __name__ == '__main__':
   app.run(host="0.0.0.0")
   