from bottle import route, get, post, run, request, redirect, response
from json import dumps, loads

x = -1
y = -1

@post('/')
def process():
    try:
      global x, y
      # print(request.forms.get())
      data = loads(request.body.read())
      x = float(data['x'])
      y = float(data['y'])
    except ValueError:
      pass

@get('/')
def return_data():
    rv = {'x': x, 'y': y}
    response.content_type = 'application/json'
    return dumps(rv)

run(host='caroline.dyn.wpi.edu', port=8000, debug=True, reloader=True)
