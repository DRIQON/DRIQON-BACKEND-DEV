import psycopg
from config import *

def connect_sql():
   connection = psycopg.connect(
        host=POSTGRES_HOST,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=POSTGRES_PORT
    )
   print("Connected Successfully!")
   return connection