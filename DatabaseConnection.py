import psycopg2

# connect() actually helps us to connect to the db
conn = psycopg2.connect(dbname="postgres", user="postgres", password="@Intrtp21!", host="localhost", port="5432")

# to execute a query we need to create a cursor
cur = conn.cursor()
cur.execute('''CREATE TABLE student(ID Serial, NAME text, ADDRESS text, AGE text);''')

print("Table created")
# you also need to commit the connection and then close the connection
conn.commit()
conn.close()