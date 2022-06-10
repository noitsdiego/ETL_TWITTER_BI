import twitter_etl_extract_helper
import twitter_etl_transform_helper
import twitter_etl_load_helper


tweets_search = twitter_etl_extract_helper.extraerDatosDesdeBusqueda("#EleccionesColombia2022")
dfTweets = twitter_etl_transform_helper.obtenerTweets(tweets_search)
dfTweetsRT = twitter_etl_transform_helper.obtenerTweetRT(dfTweets)
dfTweetsDeVerificados = twitter_etl_transform_helper.obtenerTweetVerficados(dfTweets)
dfTweetsDeNoVerificados = twitter_etl_transform_helper.obtenerTweetNoVerficados(dfTweets)
dfTweetsOriginal = twitter_etl_transform_helper.obtenerTweetOrginal(dfTweets)

dfTweets.to_csv("Alltweet.csv", header=False, sep=';',mode='a')


twitter_etl_load_helper.guardarBaseDeDatos(dfTweets,"tweets")
twitter_etl_load_helper.guardarBaseDeDatos(dfTweetsRT,"tweets_RT")
twitter_etl_load_helper.guardarBaseDeDatos(dfTweetsDeVerificados,"tweets_De_Verificados")
twitter_etl_load_helper.guardarBaseDeDatos(dfTweetsDeNoVerificados,"tweets_De_No_Verificados")
twitter_etl_load_helper.guardarBaseDeDatos(dfTweetsOriginal,"tweets_Originales")
