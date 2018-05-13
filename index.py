from bottle import mako_view as view
from bottle import Bottle,route,run,template

app=Bottle()

# home page #
@app.route('/home/')
@view('home')
def home():
  return {}

# profile page #
@app.get('/profile/')
@view('profile')
def profile():
  return {}

# info page #
@app.get('/info/')
@view('info')
def info():
  return {}

# form page #
@app.get('/form/')
@view('form')
def form():
  return {}

if __name__ == "__main__":
  run(app=app, host="0.0.0.0", port='8080')
