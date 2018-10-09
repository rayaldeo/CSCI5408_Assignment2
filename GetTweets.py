import tweepy
import csv
import re

# Giving the Twitter API Credentials
consumer_key = "4lBkFFX92TD7c8iz53s9piLnA"
consumer_secret = "eXTYXph2GaArf5w154sK6Jq5kJpL724C0CNZntVxxbscopQvld"
access_key = "1290476449-Rsv7ODyJeRyQgnsJ3WV0zQOZohxGAGbwERIy1r5"
access_secret = "RHhnwTr2JbFVuegWESjhPR3ZKWpmCGei6ji3iUaDLkBF5"

# To establish connection with Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Remove the already created CSV file 
#os.remove("tweets.csv")
tweets_list = []


# Cleaning the tweets
def clean_tweets(tweet):
    #Remove Links
    tweet = re.sub(r"http\S+", "", tweet)
    #remove unicodes
    tweet = ''.join([c for c in tweet if ord(c) < 128])
    #removing @mentions
    tweet = re.sub(r'@[A-Za-z0-9]+','',tweet)
    #removing hastags
    tweet = re.sub(r'#[A-Za-z0-9]+','',tweet)
    #removing speacial characters
    tweet = re.sub('[^A-Za-z0-9]+', ' ',tweet)
    #Remove extra Spaces
    tweet = re.sub(r' +', ' ', tweet)
    tweet = tweet.lstrip()
    return tweet


# Writing into a CSV file
def write_tweet(tweet):
    try:
        outfile = open('tweets.csv','a',encoding='utf-8',newline='')
        writer = csv.writer(outfile,delimiter=',')
        writer.writerow([tweet])
    except e:
        print("Error.." + str(e))


# To search for Tweets of each users and append it to CSV file
def get_tweets():
    try:
        for tw in tweepy.Cursor(api.user_timeline, id="realDonaldTrump", exclude_replies = True).items(1300):
        #tw = api.search(search_tag,lang="en",count="100")
            tweets_list.append(tw.text)
    except tweepy.error.TweepError as e:
            print("Error.. " + str(e))

# List to fetch 1000 tweets from different Users
#search_list= ["Dhoni","Apple","Vijay","sachin_rt","Raina","Carl Pei", "Cristiano Ronaldo","Messi","ESPNcricinfo","Oneplus","chilluvandu","Elon Musk","Twitter","Jaguar","Audi"]

#for search_tag in search_list:
get_tweets()

for tweet in tweets_list:
    if 'RT ' not in tweet:
        cleaned_tweets = clean_tweets(tweet)
        write_tweet(cleaned_tweets)
        




