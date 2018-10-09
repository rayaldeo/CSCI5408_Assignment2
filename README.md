# CSCI5408_Assignment2
# Task Description:

For this assignment,we wanted to learn how to extract,transform and load data from Twitter api. For the extraction, we needed a Twitter developer account that would give up access to Twitter’s API. It took a few days for our Twitter account application to be accepted.Once accepted, we were able to use consumer API key,access token, and access token secret to extract tweets from Twitter. We used python for all of our code snippets and it would be used to help describe our process.Once the tweets were extracted from Twitter, we had to write a function that would clean up the tweets. We didn’t want any tweets that had a , “#Something”, e.g. #TimesUp. We also didn’t want tweets with links to images or other web pages.These things would dirty our data.Once the tweets were cleaned up, we performed the sentiment analysis using SocialSent[1]. Every word in a tweet was analyzed and a cumulative score was returned in a CSV file as well as the tweet and overall sentiment.

For Elasticsearch,we used the IBM Cloud.We took the csv file and converted into json; data that Elasticsearch can accept.The algorithm for uploading our data presented some issues but we were able to remedy them.Once the data was uploaded, we were able to perform query searches of our data.

Python Files:

 - Csv_to_json : Converts CSV files to JSON.
 - ElasticSearch : Uploads analized tweets to Elasticsearch.
 - GetTweets : Gets Tweets from Twitter API.
 - Lexicon_Analysis : Runs sentiment analysis on tweets.
 - queryonelastic: Runs query searches through elasticsearch.

# References

[1] W. Hamilton and K. Clark, "williamleif/socialsent", GitHub, 2018. [Online]. Available: https://github.com/williamleif/socialsent. [Accessed: 03- Oct- 2018].

[2] Elasticsearch-py.readthedocs.io. (2018). Python Elasticsearch Client — Elasticsearch 6.3.0 documentation. [online] Available at: https://elasticsearch-py.readthedocs.io/en/master/ [Accessed 5 Oct. 2018].

[3] GitHub. (2018). stepthom/lexicon-sentiment-analysis. [online] Available at: https://github.com/stepthom/lexicon-sentiment-analysis [Accessed 7 Oct. 2018].

[4] Docs.python.org. (2018). The Python Tutorial — Python 3.7.1rc1 documentation. [online] Available at: https://docs.python.org/3/tutorial/index.html [Accessed 3 Oct. 2018].


