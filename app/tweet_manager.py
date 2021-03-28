import pysolr
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd


class TweetManager:
    solr = pysolr.Solr('http://localhost:8983/solr/luck', always_commit=True)
    solr.optimize()
    
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
    
    @staticmethod
    def rank_tweets(search_query, tweets):
        tweet_content = [tweet['content'][0] for tweet in tweets]
        vectorizer = TfidfVectorizer()
        content = tweet_content.copy()
        content.insert(0, search_query)
        vectors = vectorizer.fit_transform(content)
        feature_names = vectorizer.get_feature_names()
        dense = vectors.todense().tolist()
        
        query_tfidf = pd.DataFrame([dense[0]], columns=feature_names)
        document_tfidf = pd.DataFrame(dense[1:], columns=feature_names)
        
        all_scores = list(document_tfidf.dot(query_tfidf.iloc[0]))
        for i in range(len(all_scores)):
            all_scores[i] = [i, all_scores[i]]
        all_scores = np.array(all_scores)
        all_scores = all_scores[all_scores[:, 1].argsort()][::-1]

        ranked_tweets = []
        for score in all_scores:
            tweet = tweets[int(score[0])]
            ranked_tweets.append(tweet)
        return tweets
    
    @staticmethod
    def extract_tweets(query):
        tweets = TweetManager.get_tweets_by_exact_match(query)
        if len(tweets) != 10:
            similar_tweets = TweetManager.get_tweets_by_similarity(query)
            tweets = tweets + similar_tweets[:10-len(similar_tweets)]
        if len(tweets) == 0:
            return []
        ranked_tweets = TweetManager.rank_tweets(query, tweets)
        return ranked_tweets