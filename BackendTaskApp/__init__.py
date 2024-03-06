from flask import Flask
import psycopg2

#Flask Decleration
app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkey"

#DB Decleration
DB_NAME = "assignment"
DB_USER = "postgres"
DB_PASS = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
except Exception as DATABASE_CONNECTION_ERROR:
    print(DATABASE_CONNECTION_ERROR)


cursor = conn.cursor()

from BackendTaskApp import views