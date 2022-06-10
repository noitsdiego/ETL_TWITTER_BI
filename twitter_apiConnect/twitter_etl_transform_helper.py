import pandas as pd
import twitter_etl_clean

columnas = ['USUARIO','ESTA VERIFICADO','SEGUIDORES','TWEETS REALIZADOS',
            'FECHA','TWEET ACTUAL','REALIZADO EN','NUMERO DE RETWEET','NUMERO DE LIKES']

def obtenerTweets(tweets_search):
    data = []
    for tweet in tweets_search:
        texto = twitter_etl_clean.limpiarTexto(tweet.full_text)
        data.append([tweet.user.screen_name, tweet.user.verified , tweet.user.followers_count, tweet.user.statuses_count, 
                 tweet.created_at,texto, tweet.source, tweet.retweet_count, tweet.favorite_count])
    return (pd.DataFrame(data, columns=columnas))

def obtenerTweetRT(dfTotal):
    data = []
    for i in range(len(dfTotal)): 
        if((dfTotal.loc[i,"TWEET ACTUAL"]).__contains__('RT @')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas) 

def obtenerTweetVerficados(dfTotal):
    data = []
    for i in range(len(dfTotal)): 
        if(str(dfTotal.loc[i,"ESTA VERIFICADO"]).__contains__('True')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas)   

def obtenerTweetNoVerficados(dfTotal):
    data = []
    for i in range(len(dfTotal)): 
        if(str(dfTotal.loc[i,"ESTA VERIFICADO"]).__contains__('False')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas)

def obtenerTweetOrginal(dfTotal):
    data = []
    for i in range(len(dfTotal)): 
        if(not (dfTotal.loc[i,"TWEET ACTUAL"]).__contains__('RT @')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas) 