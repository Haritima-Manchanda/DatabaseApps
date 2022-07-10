import psycopg2

# connect() actually helps us to connect to the db
conn = psycopg2.connect(dbname="postgres", user="postgres", password="@Intrtp21!", host="localhost", port="5432")
print("Connection Successful")