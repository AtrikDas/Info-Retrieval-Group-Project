import pysolr
import logging

class TweetManager:
    solr = pysolr.Solr('http://localhost:8983/solr/luck', always_commit=True)

    @staticmethod
    def get_tweets_by_exact_match(query):
        try:
            response = TweetManager.solr.search(query)
        except:
            logging.error("Error in getting tweets by exact match")
            return []
        tweets = list(map(lambda x: x, response))
        return tweets
    
    @staticmethod
    def get_tweets_by_similarity(query):
        try:
            response = TweetManager.solr.more_like_this(q = query, mltfl='text')
        except:
            logging.error("Error in getting tweets by similarity")
            return []
        tweets = list(map(lambda x: x, response))
        return tweets
