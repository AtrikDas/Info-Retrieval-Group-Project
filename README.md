# Information Retrieval System

CZ4034 - Information Retrieval

Twitter News Retrieval System on the US Presedential Elections 2020

This project contains 3 main sections
1. Crawling

    We utilized snscrape to crawl Twitter and collected tweets regarding the US Presedential Elections from various countries.
    The Crawled data had the following columns:
    | Field Name | Description |
    | ---------- | ----------- |
    | username   | Contains the username of the user that posted the tweet|
    | content    | Contains the actual tweet|
    | date       | Contains the date on which the tweet was posted|
    | country    | Contains the country where the user lives in|
    | replycount | Contains the number of people that commented on the tweet|
    | retweetcount| Contains the number of people that shared that particular tweet|
    | likecount  | Contains the number of people that liked that particular tweet|
<br/>

2. Indexing and Querying
    
    Indexing is a way to optimize the performance of a database by minimizing the number of disk accesses required when a query is processed.  We created an inverted index using Solr to optimize the search
    process. Inverted index helps optimizing the search process and allows fast full text search, at a cost of increased processing when a document is added.

    We also incorporated the spell check feature into our system which was implemented with the help of the n-grams algorithm.

3. Sentiment Analysis

    Model Performance:
    | Model | F1 Score | Accuracy | Precision | Recall |
    | ----- | -------- | -------- | --------- | ------ |
    | Bert  | 0.74490  | 0.73737  | 0.75258   | 0.73737 |
    

    We also implemented a weighted sentiment analysis model which would evalutate the sentiment score based on the number of likes, comments and retweets. This helped us calculate the influence each tweet had. To find out more on this, click [here](./docs/report.pdf)
<br/>

## Quickstart

To start solr:

```bash
cd solr
./bin/solr start
```

To start the flask app:

```bash
cd app
pip install -r requirements.txt
python app.py
```
