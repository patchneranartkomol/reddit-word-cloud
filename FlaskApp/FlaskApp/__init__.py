from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'TopSecretKey' #TODO: stubbed for testing, move this to ignored config file

class BasicForm(FlaskForm):
	username = StringField('username')


@app.route('/', methods=['GET', 'POST'])
def homepage():
	form = BasicForm()
	return render_template("index.html", form=form)

@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run()
	  
