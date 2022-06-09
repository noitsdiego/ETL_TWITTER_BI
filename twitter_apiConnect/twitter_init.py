import tweepy
from unicodedata import normalize
import re
import pandas as pd

api_key = ""
api_key_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets_search = api.search_tweets("Colombia", tweet_mode="extended")

columnas = ['USUARIO','RT','VERFICACION','SEGUIDORES','TWEETS REALIZADOS',
            'TWEET ACTUAL','REALIZADO EN','ES RESPUESTA', 'LUGAR','NUMERO DE RETWEET','NUMERO DE LIKES']
data = []

for tweet in tweets_search:
    
    texto = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", tweet.full_text), 0, re.I
    )
    
    if(texto.__contains__('@') and texto.__contains__('RT') and texto.__contains__(':')) :
        texto = texto.split(':')[1]
        
    texto = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', texto)
    texto = re.sub(r"  +", ' ', texto)
    
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    
    texto = emoji_pattern.sub(r'', texto)
    texto = re.sub(r'[^\s][...]+', '',texto)

    data.append([tweet.user.screen_name, tweet.is_quote_status, tweet.user.verified , tweet.user.followers_count, tweet.user.statuses_count, 
                 texto, tweet.source, tweet.in_reply_to_status_id, tweet.place, tweet.retweet_count, tweet.favorite_count])
    
    
df = pd.DataFrame(data, columns=columnas)


df.to_csv('tweet.csv', sep=';')