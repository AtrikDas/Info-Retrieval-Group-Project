from flask import Flask, render_template, request, send_file, send_from_directory
import os
from utils import filter
import os

BASE_DIR = os.getcwd()

application = Flask(__name__)

PORT = os.getenv('PORT', 8000)


@application.route("/")
def index():
    return render_template('pages/index.html')


@application.route("/search")
def search():
    return render_template('pages/search.html')


@application.route("/searchResults")
def search_results():
    search_query = request.args.get("search")
    if search_query:
        text = "content:" + search_query
        tweets, suggestions = filter(text)
        
        if len(suggestions) == 0:
            suggestions = []
        if len(tweets) == 0:
            return render_template('pages/search.html', search_query = search_query, error = "No tweets Found", tweets = None, suggestions=suggestions)
        return render_template('pages/search.html', search_query = search_query, error= None, tweets = tweets, suggestions=suggestions)

    return render_template('pages/search.html')


@application.route("/map")
def geospatial_search2():
    return render_template("pages/map.html")


# @application.route("/plotly/<filename>")
# def plotly(filename):
#     return send_from_directory(f"{BASE_DIR}/js/", filename=filename)


if __name__ == "__main__":
    print(BASE_DIR)
    application.run(debug=True, port=PORT)
