from tweet_manager import TweetManager
import plotly.express as px

def filter(search_query, ranking= None, countries = []):
    countries = "(" +" OR ".join(countries) + ")"
    tweets = TweetManager.extract_tweets(search_query, countries)
    spellcheck_suggestions = TweetManager.spell_check(search_query)

    if ranking == "Most Relevant":
        tweets = TweetManager.rank_by_most_relevant_tweets(search_query, tweets)
    elif ranking == "Date":
        tweets = TweetManager.rank_by_date_tweets(tweets)
    elif ranking == "Likes":
        tweets = TweetManager.rank_by_likes_tweets(tweets)
    elif ranking == "Retweets":
        tweets = TweetManager.rank_by_retweets_tweets(tweets)

    return tweets[:15] if len(tweets) > 15 else tweets, spellcheck_suggestions


def geospatial_graph():
    df = px.data.gapminder().query("year==2007")
    fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
    # fig.show()
    # fig.write_html("1.html")
    # return html.Div([dcc.Graph(figure=fig)])


if __name__ == "__main__":
    print(filter("trump"))