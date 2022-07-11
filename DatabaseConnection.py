import psycopg2

def create_table():
    # connect() actually helps us to connect to the db
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="@Intrtp21!", host="localhost", port="5432")

    # to execute a query we need to create a cursor
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student(ID Serial, NAME text, ADDRESS text, AGE text);''')

    # you also need to commit the connection and then close the connection
    conn.commit()
    conn.close()

def insert_data():
    name = input("Enter student name: ")
    address = input("Enter student address: ")
    age = input("Enter student age: ")

    conn = psycopg2.connect(dbname="postgres", user="postgres", password="@Intrtp21!", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''INSERT INTO STUDENT(NAME, ADDRESS, AGE) VALUES (%s, %s, %s)'''
    cur.execute(query, (name, address, age))
    conn.commit()
    conn.close()

#create_table()
insert_data()