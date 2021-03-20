from tweet_manager import TweetManager
import plotly
import json
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

def filter(search_query):
    exact_match_tweets = TweetManager.get_tweets_by_exact_match(search_query)
    if len(exact_match_tweets) >= 5:
        return exact_match_tweets[:5]
    similar_tweets = TweetManager.get_tweets_by_similarity(search_query)
    return exact_match_tweets + similar_tweets[:6-len(similar_tweets)]


def geospatial_graph():
    df = px.data.gapminder().query("year==2007")
    fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
    # fig.show()
    fig.write_html("1.html")
    return html.Div([dcc.Graph(figure=fig)])