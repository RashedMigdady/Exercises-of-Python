from flask import Flask ,render_template

app = Flask(__name__)

'''
@app.route('/<user>')
def fullname(user):
    user2 = {"username":"ahmad"}
    return render_template("index1.html" ,title="MyPage", name = user , user2 = user2)

@app.route('/index')
def hello_world():
    return "<html><body><h1> Rashed m </h1> </body></html>"

@app.route('/hello/<name>')
def h_n(name):
    return "hello %s !" % name
'''
@app.route('/r/<int:score>')
def test(score):
    return render_template('index1.html' , mark = score)

if __name__=='__main__':
    app.run(debug = True)