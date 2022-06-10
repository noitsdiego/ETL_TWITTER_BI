from urllib.parse import quote_plus as urlquote
import psycopg2
from sqlalchemy import create_engine

def guardarBaseDeDatos(df, nameTable):
    conn = psycopg2.connect(host="localhost", port = "5432", dbname = "postgres", user = "postgres", password = "1234")
    cur = conn.cursor()
    engine = create_engine('postgresql://postgres:%s@localhost:5432/postgres' %urlquote('1234'))
    df.to_sql(name = nameTable, con = engine, if_exists='append', index= False)
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.close()
    
    
def guardarBaseDeDatosAWS(df, nameTable):
    conn = psycopg2.connect(host="etl-twitter.cgyicsjyl7q5.sa-east-1.rds.amazonaws.com", port = "5432", dbname = "etltwitter"
                            , user = "postgres", password = "admin1234")
    cur = conn.cursor()
    engine = create_engine('postgresql://postgres:%s@etl-twitter.cgyicsjyl7q5.sa-east-1.rds.amazonaws.com:5432/etltwitter'
                           %urlquote('admin1234'))
    df.to_sql(name = nameTable, con = engine, if_exists='append', index= False)
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.close()   