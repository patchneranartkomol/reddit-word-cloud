from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from .comment_reader import init_reddit, get_redditor, get_comments_from_redditor


app = Flask(__name__)
app.config['SECRET_KEY'] = 'TopSecretKey' #TODO: stubbed for testing, move this to ignored config file

class BasicForm(FlaskForm):
	username = StringField('username', [validators.InputRequired()])


@app.route('/', methods=['GET'])
def homepage():
	username = request.args.get('username')
	if username is not None:
		reddit = comment_reader.init_reddit()
		redditor = get_redditor(username, reddit)
		comments = comment_reader.get_comments_from_redditor(redditor, reddit)
		comment_string = "|".join(comments)
		return comment_string
	else:
		form = BasicForm()
		return render_template("index.html", form=form)

@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run()
	  
