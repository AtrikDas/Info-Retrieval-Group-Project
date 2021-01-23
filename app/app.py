from flask import Flask, render_template
import os

application = Flask(__name__)

PORT = os.getenv('PORT', 8000)


@application.route("/")
def index():
    return render_template('pages/about.html')


@application.route("/search")
def search():
    return render_template('pages/search.html')


@application.route("/search_results")
def search_results():
    return render_template('pages/search_results.html')


@application.route("/sentiment")
def about():
    return render_template('pages/sentiment_analysis.html')


if __name__ == "__main__":
    application.run(debug=True, port=PORT)
