__author__ = "Fernando Talavera"
__name__ = "Práctica 3"

from flask import Flask, render_template, session, redirect, url_for, escape, request
import pickle
from pathlib import Path
import os

app = Flask(__name__, template_folder='./templates/')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def recentlist(value):
    if len(list) >= 3:
        list.pop(-1)

    list.insert(0,value)

def connect():
    D = {}
    
    my_file = Path("./d.dat")
    
    if not my_file.exists():
       os.mknod("./d.dat")

    if os.stat(my_file).st_size != 0:
        # Cargar el archivo
        with open('d.dat', 'rb') as f:
	        D = pickle.load(f)
    else:
        # Crear el archivo
        with open('d.dat', 'wb') as f:
	        pickle.dump(D, f)

    return D

@app.route('/')
def index():
    if session:
        if 'registered' in session:
            return render_template('index.html', usuario=None, signup=True)
        elif 'username' in session:
            return render_template('index.html', usuario=escape(session['username']), recents=list)
    else:
        return render_template('index.html', usuario=None, signup=True)
    
@app.route('/menu1')
def menu1():
    if session: 
        if 'registered' in session:
            session.pop('registered', None)
            return render_template('menu1.html', usuario=None, signup=True)
        elif 'username' in session:
            recentlist('menu1')
            return render_template('menu1.html', usuario=escape(session['username']), recents=list)
    else:
        return render_template('menu1.html', usuario=None, signup=True)

@app.route('/menu2')
def menu2():
    if session: 
        if 'registered' in session:
            session.pop('registered', None)
            return render_template('menu2.html', usuario=None, signup=True)
        elif 'username' in session:
            recentlist('menu2')
            return render_template('menu2.html', usuario=escape(session['username']), recents=list)
    else:
        return render_template('menu2.html', usuario=None, signup=True)

@app.route('/menu3')
def menu3():
    if session:
        if 'registered' in session:
            session.pop('registered', None)
            return render_template('menu3.html', usuario=None, signup=True)
        elif 'username' in session:
            recentlist('menu3')
            return render_template('menu3.html', usuario=escape(session['username']), recents=list)
    else:
        return render_template('menu3.html', usuario=None, signup=True)

@app.route('/profile', methods=['GET','POST'])
def profile():
    if session:
        if 'username' in session:
            return render_template('profile.html', usuario=escape(session['username']), contrasenia=escape(session['password']), recents=list)
    else:
        return redirect(url_for('index'))

@app.route('/editprofile', methods=['GET','POST'])
def editprofile():
    if session:
        if 'username' in session:
            return render_template('editprofile.html', usuario=escape(session['username']))
    else:
        return redirect(url_for('index'))

@app.route('/modify', methods=['GET','POST'])
def modify():
    session.pop('failed', None)
    username = request.form['username']
    password = request.form['password']

    D = connect()

    if username == session['username']:
        D[username] = password
        
        session['username'] = username
        session['password'] = password
        
        with open('d.dat', 'wb') as f:
	        pickle.dump(D, f)

        return redirect(url_for('index'))
    else:
        if not username in D:
            D[username] = D[session['username']]
            del D[session['username']]
            D[username] = password

            session['username'] = username
            session['password'] = password

            with open('d.dat', 'wb') as f:
	            pickle.dump(D, f)
            
            return redirect(url_for('index'))
        else:
            session['failed'] = True
            return redirect(url_for('editprofile'))


@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('singup.html', signup=False)

@app.route('/register', methods=['GET','POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    D = connect()
    
    if not username in D:
        session.pop('failed', None)
        session['registered'] = True
        D.update({username: password})

        with open('d.dat', 'wb') as f:
	        pickle.dump(D, f)
        
        session['username'] = username
        session['password'] = password

        return redirect(url_for('index'))
    else:
        session['failed'] = True
        return redirect(url_for('signup'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        D = connect()
        
        if username in D and D[username] == password:
            session['username'] = username
            session['password'] = password
            session.pop('registered',None)
            global list
            list=[]
        
        return redirect(url_for('index'))
    
@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('username', None)
    session.pop('password', None)

    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)