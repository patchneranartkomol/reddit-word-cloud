from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

from .comment_reader import init_reddit, get_redditor, get_comments_from_redditor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TopSecretKey' #TODO: stubbed for testing, move this to ignored config file

class BasicForm(FlaskForm):
	username = StringField('username', validators=[InputRequired()])


@app.route('/', methods=['GET'])
def homepage():
	username = request.args.get('username')
	form = BasicForm()
	if username is not None:
		reddit = comment_reader.init_reddit()
		redditor = get_redditor(username, reddit)
		try:
			comments = comment_reader.get_comments_from_redditor(redditor, reddit)
		except NameError:
			return render_template("index_alert.html", alert_body='User not found. Please try again.', form=form)
		comment_string = "|".join(comments)
		return render_template("index_content.html", comment_data=comment_string, form=form)
	else:
		return render_template("index.html", form=form)

@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run()
	  
