from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

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

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
