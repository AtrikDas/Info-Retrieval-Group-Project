from tweet_manager import TweetManager
import plotly
import json
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import math 

def filter(search_query):
    exact_match_tweets = TweetManager.get_tweets_by_exact_match(search_query)
    similar_tweets = TweetManager.get_tweets_by_similarity(search_query)
    all_tweets = exact_match_tweets + similar_tweets[:6-len(similar_tweets)]
    ranked_tweets = rank_tweets(search_query, all_tweets)
    return all_tweets


def geospatial_graph():
    df = px.data.gapminder().query("year==2007")
    fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
    # fig.show()
    # fig.write_html("1.html")
    return html.Div([dcc.Graph(figure=fig)])

def rank_tweets(search_query, tweets):
    all_tweets = [tweet['content'] for tweet in tweets]
    all_words = set()
    all_content = [search_query] + all_tweets
    for content in all_content:
        content = content[0]
        content = content.split(' ')
        for word in content:
            all_words.add(word)
    print(len(all_words))

    return tweets

def calculate_term_frequency(content, all_words):
    tf = {}
    for word in content:
        if word in tf:
            tf[word] += 1
        else:
            tf[word] = 1
    for word in all_words:
        if word not in tf:
            tf[word] = 0

    for key in tf.keys:
        tf[key] = 1 + math.log(tf[key])
    return tf

def document_frequency(tweets, ):
    pass

if __name__ == "__main__":
    filter("trump")