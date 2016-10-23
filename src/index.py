from flask import Flask, url_for, json, render_template
app = Flask(__name__)

# loading json
def showjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/js/", "films.json")
    data = json.load(open(json_url))
    return render_template('showjson.html', data=data)

@app.route("/")
def index():
  films = ['Comedies', 'Drama', 'Animation', 'Sci-fi']
  return render_template('index.html', title='Home', films=films),200

@app.route('/Comedies/')
def Comedies():
  return render_template('comedies.html', title='Comedies')

@app.route('/Drama/')
def Drama():
  return render_template('drama.html', title='Drama')

@app.route('/Animation/')
def Animation():
  return render_template('animation.html', title='Animation')

@app.route('/Sci-fi/')
def Scifi():
  return render_template('scifi.html', title='Animation')

@app.errorhandler (404)
def page_not_found (error):
  return render_template('404.html', title='Error'), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)