from tweet_manager import TweetManager

def filter(search_query):
    exact_match_tweets = TweetManager.get_tweets_by_exact_match(search_query)
    if len(exact_match_tweets) >= 5:
        return exact_match_tweets[:5]
    similar_tweets = TweetManager.get_tweets_by_similarity(search_query)
    return exact_match_tweets + similar_tweets[:6-len(similar_tweets)]