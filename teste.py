# import the module
import tweepy

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# fetching the trends
trends = api.available_trends()

print("The number of locations available are : " + str(len(trends)))
