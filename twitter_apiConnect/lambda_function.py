import json

import twitter_etl_extract_helper
import twitter_etl_transform_helper

#Funcion lambda de AWS encargada de realizar la busqueda de tweets

def lambda_handler(event, context):
    
    tweets_search = twitter_etl_extract_helper.extraerDatosDesdeBusqueda("#EleccionesColombia2022")
    dfTweets = twitter_etl_transform_helper.obtenerTweets(tweets_search)
    dfTweetsRT = twitter_etl_transform_helper.obtenerTweetRT(dfTweets)
    dfTweetsDeVerificados = twitter_etl_transform_helper.obtenerTweetVerficados(dfTweets)
    dfTweetsDeNoVerificados = twitter_etl_transform_helper.obtenerTweetNoVerficados(dfTweets)
    dfTweetsOriginal = twitter_etl_transform_helper.obtenerTweetOrginal(dfTweets)



    print(dfTweetsOriginal)    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(tweepy.__version__)
    }