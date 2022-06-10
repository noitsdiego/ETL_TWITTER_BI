import tweepy

api_key = "Ip9pdpfh8UHnEss1JkWHrKDRZ"
api_key_secret = "TZA1066NoRZBPczJsRK7IZ0adxZVHsU6rhIuFW26xLAvpt74bx"

access_token = "1350080036-A2GKe8RnEdmwdwjmw0RVmuchN6qzvo55ViZgJmR"
access_token_secret = "hszrFxwzN2DUCVOxLNxeYawi2CaaethCHiJqhEVoSX2HC"

def extraerDatosDesdeBusqueda(tema):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets_search = api.search_tweets(tema, tweet_mode="extended")
    
    return tweets_search