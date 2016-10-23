from flask import Flask, render_template
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

app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.ico'))
                 
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
