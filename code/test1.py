# import requests as rq
# import pandas as pd
# import json as jsn

# #url = 'https://rds.sa-east-1.amazonaws.com'

# url = 'https://rds.sa-east-1.amazonaws.com/hpsaws.cpz5mncc2ufk.sa-east-1.rds.amazonaws.com:3306'

# res = rq.get(url)

# df = pd.DataFrame(res)

# print(df.columns)


import mysql.connector
import sys
import boto3
import os

ENDPOINT="hpsaws.cpz5mncc2ufk.sa-east-1.rds.amazonaws.com"
PORT="3306"
USER="admin"
REGION="sa-east-1"
DBNAME="WS_HPS"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds', region_name="sa-east-1")

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=token, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))          
                