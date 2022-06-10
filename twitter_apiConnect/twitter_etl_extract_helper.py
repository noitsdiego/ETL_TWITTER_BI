import tweepy

api_key = ""
api_key_secret = ""

access_token = ""
access_token_secret = ""

def extraerDatosDesdeBusqueda(tema):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets_search = api.search_tweets(tema, tweet_mode="extended")
    
    return tweets_search