import twitter_etl_extract_helper
import twitter_etl_transform_helper
import twitter_etl_load_helper


tweets_search = twitter_etl_extract_helper.extraerDatosDesdeBusqueda("#EleccionesColombia2022")
dfTweets = twitter_etl_transform_helper.obtenerTweets(tweets_search)

dfTweets.to_csv("Alltweet.csv", sep=";");

twitter_etl_load_helper.guardarBaseDeDatos(dfTweets,"tweets")
