from flask import Flask
app = Flask(__name__)
# =============================================================================
# app = Flask(__name__)
# 
# @app.route('/')
# def hello_world():
#     return 'Hello world!'
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================


# =============================================================================
# app = Flask(__name__)
# 
# @app.route('/')
# @app.route('/index')
# 
# def index():
#     return 'Hello world!'
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================

# =============================================================================
# app = Flask(__name__)
# 
# @app.route('/')
# 
# def index():
#     return '<html><body><h1> Rashed </h1></body></html>'
# 
# if __name__ == '__main__':
#     app.run()
# 
# =============================================================================

# =============================================================================
# @app.route('/')
# def index():
#     return 'Index!'
# 
# @app.route('/hello')
# def hello():
#     return 'Hello world!'
# 
# @app.route('/members')
# def members():
#     return 'Members'
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================

# =============================================================================
# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello %s!' %name
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================

# =============================================================================
# from flask import Flask, render_template
# app = Flask(__name__)
# 
# @app.route('/')
# def index():
#     return render_template('index.html')
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================


from flask import Flask, render_template
# =============================================================================
# app = Flask(__name__)
# 
# @app.route('/hello/<user>')
# def hello_name(user):
#     return render_template('index.html', name = user)
# 
# if __name__ == '__main__':
#     app.run()
# 
# =============================================================================

# =============================================================================
# app = Flask(__name__)
# 
# @app.route('/')
# @app.route('/index')
# 
# def index():
#     user = {'username' : 'Academy'}
#     return render_template('index1.html', title = 'Home', user = user)
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================

# =============================================================================
# app = Flask(__name__)
# 
# @app.route('/hello/<int:score>')
# def hello_name(score):
#     return render_template('index2.html', marks = score)
# 
# if __name__ == '__main__':
#     app.run()
# 
# =============================================================================

# =============================================================================
# @app.route('/')
# def index():
#     return render_template('index3.html')
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================

# =============================================================================
# @app.route('/')
# def index():
#     return render_template('index4.html')
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================

from flask import Flask, redirect, url_for
# =============================================================================
# app = Flask(__name__)
# 
# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin'
# 
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'Hello %s as Guest' % guest
# 
# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin' :
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest = name))
#     
# if __name__ == '__main__':
#     app.run()
# =============================================================================

# =============================================================================
# @app.route('/')
# def index():
#     return render_template('index5.html')
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================

# =============================================================================
# @app.route('/')
# def hello():
#     message = 'hello, world'
#     return render_template('index6.html', message = message)
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================

@app.route('/')
def index():
    return render_template('index6.html')

if __name__ == '__main__':
    app.run()
