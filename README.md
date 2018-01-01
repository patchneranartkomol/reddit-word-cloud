# Reddit Word Cloud

This is a Flask Application that will generate a word cloud given any Reddit username. Here's an example of my application, deployed on [Heroku](https://reddit-word-cloud.herokuapp.com)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3
* A Reddit account with devel, including a unique Client key and Client secret for API Script access

### Installing

* Clone this git repository.
* PIP Install all dependencies in requirements.txt
* Place your unique Client key and secret in your praw.ini file
* To run locally:

```
export FLASK_APP=app.py
flask run
```

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [PRAW](http://praw.readthedocs.io/en/latest/getting_started/quick_start.html) - Python Reddit API Wrapper
* [d3-cloud](https://github.com/jasondavies/d3-cloud) - Used to generate word clouds

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Credit to Jason Davies for the D3.js word cloud library used in this project https://github.com/jasondavies/d3-cloud
