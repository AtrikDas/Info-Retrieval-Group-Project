from tweet_manager import TweetManager
from geospatial_graph import Geospatial_Graph

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
    fig = Geospatial_Graph.generate_graph()
    ig.show()


if __name__ == "__main__":
    print(filter("trump"))