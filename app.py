from bottle import route, run, template, static_file, error, request
import os

@route('/')
def index():
    return template('index')

@route('/a')
def lidura():
    return template('lidura')

@route('/b')
def lidurb():
    return  template('lidurb')
"""
@route('/c')
def lidurc():
    return  template('lidurc')

@route('/d')
def lidurd():
    return  template('lidurd')

@route('/new_user', method="POST")
def new_user():
    email = request.forms.email
    user = request.forms.user
    password = request.forms.password
    return template('new_user', email=email, user=user, password=password)

@route('/konnun')
def konnun():
    nickname = request.query.nickname
    dog = request.query.dog
    movie = request.query.movie
    zodiac = request.query.zodiac
    age = int(request.query.age)

    return template('konnun', nickname=nickname, dog=dog, movie=movie, zodiac=zodiac, age=age)

"""
#static file routing
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root ='./myfiles')

run()
#run(host='0.0.0.0',port=os.environ.get('PORT'))
