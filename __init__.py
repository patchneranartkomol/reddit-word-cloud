import json
import comment_reader

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

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
			top_comments = comment_reader.extract_top_comments_to_list(comments)
		except NameError:
			return render_template("index_alert.html", alert_body='User not found. Please try again.', form=form)
		return render_template("index_content.html", comments=json.dumps(top_comments), form=form)
	else:
		return render_template("index.html", form=form)

@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run()
