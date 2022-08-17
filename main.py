import tweepy

bearer_token = ''

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter = tweepy.API(auth)

results = twitter.search_tweets(q='PALAVRACHAVE')

dict_tweets = {}

for tweet in results:
    dict_tweets[tweet.user.screen_name] = tweet.text

print(dict_tweets)