import os
from flask import Flask, url_for, json, render_template
app = Flask(__name__)

# loading json for films page
@app.route('/Films')
def films():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "films.json")
  data = json.load(open(json_url))
  return render_template('films.html', title='VFMC', data=data)

#route for homepage
@app.route("/")
def index():
  return render_template('index.html', title='Home')

#loading json for comedies page
@app.route('/Comedies')
def comedies():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "films.json")
  comedies = json.load(open(json_url))
  return render_template('comedies.html', title='Comedies', comedies=comedies)

#loading json for drama page
@app.route('/Drama/')
def drama():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "films.json")
  drama = json.load(open(json_url))
  return render_template('drama.html', title='Drama', drama=drama)

#loading json for animation page
@app.route('/Animation/')
def animation():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "films.json")
  animation = json.load(open(json_url))
  return render_template('animation.html', title='Animation', animation=animation)

#loading json for sci-fi page
@app.route('/Sci-fi/')
def scifi():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static/js/", "films.json")
  scifi = json.load(open(json_url))
  return render_template('scifi.html', title='Sci-fi', scifi=scifi)

#route for personalised error page
@app.errorhandler (404)
def page_not_found (error):
  return render_template('404.html', title='Error'), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
