import pandas as pd
import twitter_etl_clean

columnas = ['USUARIO','ESTA VERIFICADO','SEGUIDORES','TWEETS REALIZADOS',
            'TWEET ACTUAL','REALIZADO EN','NUMERO DE RETWEET','NUMERO DE LIKES']
#Metodo encargado de obtener los tweets de personas teniendo en cuenta que se les realiza una limpieza a los datos
def obtenerTweets(tweets_search):
    data = []
    for tweet in tweets_search:
        texto = twitter_etl_clean.limpiarTexto(tweet.full_text)
        data.append([tweet.user.screen_name, tweet.user.verified , tweet.user.followers_count, tweet.user.statuses_count, 
                 texto, tweet.source, tweet.retweet_count, tweet.favorite_count])
    return (pd.DataFrame(data, columns=columnas))
#Metodo encargado de obtener los retweets de personas 
def obtenerTweetRT(dfTotal):
    data = []
    for i in range(len(dfTotal)): 
        if((dfTotal.loc[i,"TWEET ACTUAL"]).__contains__('RT @')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas) 
#Metodo encargado de obtener los tweets verificados realizando la validacion de si es o no verificado  
def obtenerTweetVerficados(dfTotal):
    data = []
    for i in range(len(dfTotal)): 
        if(str(dfTotal.loc[i,"ESTA VERIFICADO"]).__contains__('True')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas)   
#Metodo para obtener los tweets verificados que se realizan y validar si es o no verificado
def obtenerTweetNoVerficados(dfTotal):
    data = []
    for i in range(len(dfTotal)): 
        if(str(dfTotal.loc[i,"ESTA VERIFICADO"]).__contains__('False')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas)
#Metodo para obtener el tweet original del rango en donde se esta trabajando
def obtenerTweetOrginal(dfTotal):
    data = []
    for i in range(len(dfTotal)): 
        if(not (dfTotal.loc[i,"TWEET ACTUAL"]).__contains__('RT @')):
            data.append(dfTotal.loc[i])
    return  pd.DataFrame(data, columns=columnas) 