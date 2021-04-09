import pysolr
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import requests
import datetime


class TweetManager:
    solr = pysolr.Solr('http://localhost:8983/solr/final_core', always_commit=True)
    # solr.optimize()
    
    @staticmethod
    def extract_tweets(query, countries = []):
        tweets = TweetManager.get_tweets_by_exact_match(query, countries)     
        if len(tweets) == 0:
            return []
        for tweet in tweets:
            tweet['date'][0] = datetime.datetime.strptime(tweet['date'][0], "%Y-%m-%dT%H:%M:%SZ")
        return tweets

    @staticmethod
    def get_tweets_by_exact_match(query, countries = []):
        try:
            response = TweetManager.solr.search(f"content:{query}", fq=f"country:{countries}", rows=20)
        except:
            logging.error("Error in getting tweets by exact match")
            return []
        tweets = list(map(lambda x: x, response))
        return tweets

    @staticmethod
    def spell_check(query):
        try:
            url = 'http://localhost:7364/solr/final_core/spell?spellcheck.q='+query+'&spellcheck=true'
            response = requests.get(url)
            suggestions = response.json() 
            suggestions = suggestions["spellcheck"]["suggestions"][1]["suggestion"]

        except:
            logging.error("Error in getting spell check suggestions")
            return []

        return suggestions

    @staticmethod
    def rank_by_most_relevant_tweets(query, tweets):
        tweet_content = [tweet['content'][0] for tweet in tweets]
        vectorizer = TfidfVectorizer()
        content = tweet_content.copy()
        content.insert(0, query)
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
        return ranked_tweets
    
    def rank_by_date_tweets(tweets):
        return sorted(tweets, key= lambda x: x['date'][0], reverse=True)
        
    def rank_by_likes_tweets(tweets):
        try:
            return sorted(tweets, key= lambda x: x['likeCount'][0], reverse=True)
        except:
            return tweets

    def rank_by_retweets_tweets(tweets):
        try:
            return sorted(tweets, key= lambda x: x['retweetCount'][0], reverse=True)
        except:
            return tweets