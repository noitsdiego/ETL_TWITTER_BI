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

def buscarTwetts(tema):
    tweets_search = api.search_tweets(tema, tweet_mode="extended")
    
    columnas = ['USUARIO','VERFICACION','SEGUIDORES','TWEETS REALIZADOS',
            'TWEET ACTUAL','REALIZADO EN','NUMERO DE RETWEET','NUMERO DE LIKES']
    data = []
    
    for tweet in tweets_search:
        texto = limpiarTexto(tweet.full_text)
        data.append([tweet.user.screen_name, tweet.user.verified , tweet.user.followers_count, tweet.user.statuses_count, 
                 texto, tweet.source, tweet.retweet_count, tweet.favorite_count])
    
    return pd.DataFrame(data, columns=columnas)

def obtenerTweetRT(dfTotal):
    columnas = ['USUARIO','VERFICACION','SEGUIDORES','TWEETS REALIZADOS',
            'TWEET ACTUAL','REALIZADO EN','NUMERO DE RETWEET','NUMERO DE LIKES']
    data = []
    for i in range(len(dfTotal)): 
        if((dfTotal.loc[i,"TWEET ACTUAL"]).__contains__('RT @')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas) 

def obtenerTweetVerficados(dfTotal):
    columnas = ['USUARIO','VERFICACION','SEGUIDORES','TWEETS REALIZADOS',
            'TWEET ACTUAL','REALIZADO EN','NUMERO DE RETWEET','NUMERO DE LIKES']
    data = []
    for i in range(len(dfTotal)): 
        if(str(dfTotal.loc[i,"VERFICACION"]).__contains__('True')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas)   

def obtenerTweetNoVerficados(dfTotal):
    columnas = ['USUARIO','VERFICACION','SEGUIDORES','TWEETS REALIZADOS',
            'TWEET ACTUAL','REALIZADO EN','NUMERO DE RETWEET','NUMERO DE LIKES']
    data = []
    for i in range(len(dfTotal)): 
        if(str(dfTotal.loc[i,"VERFICACION"]).__contains__('False')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas)     

def obtenerTweetOrginal(dfTotal):
    columnas = ['USUARIO','VERFICACION','SEGUIDORES','TWEETS REALIZADOS',
            'TWEET ACTUAL','REALIZADO EN','NUMERO DE RETWEET','NUMERO DE LIKES']
    data = []
    for i in range(len(dfTotal)): 
        if(not (dfTotal.loc[i,"TWEET ACTUAL"]).__contains__('RT @')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas)            
             

def limpiarTexto(texto):
    texto = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", texto), 0, re.I
    )
        
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
    return texto


dfCentral = buscarTwetts("#ColombiaDecide");
dfObtenerRT = obtenerTweetRT(dfCentral)
dfTweetOriginal = obtenerTweetOrginal(dfCentral)
dfTweetDeVerificados = obtenerTweetVerficados(dfCentral)
dfTweetDeNoVerificados = obtenerTweetNoVerficados(dfCentral)
