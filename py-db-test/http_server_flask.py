from flask import Flask, request, render_template

app = Flask(__name__)


#@app.route('/<name>')
#def index(name=None):
#   return render_template('hello.html',name=name)
   
@app.route('/', methods=['GET', 'POST'])
def home():
    str = "Vol"
    li = [230,2,3,4]
    str1=random.randint(0,99)
    print(random.randint(0,99))
    return render_template('home.html',str=str,li=li,str1=str1)
	
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
   