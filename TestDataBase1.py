import sqlite3

#Creating functions
# Function for Query the DB and Return all Records

def show_all():
#Connect to DataBase
    conn = sqlite3.connect('customer.db')
#Create a cursor
    c = conn.cursor()

#Query the Database
    c.execute('SELECT rowid, * FROM customers')
    items = c.fetchall()
    for i in items:
        print(i)
#Commit our command
    conn.commit()
#Close our connextion
    conn.close

#Add a new record on the table
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute('INSERT INTO customers VALUES(?,?,?)',(first,last,email))
#Commit our command and close
    conn.commit()
    conn.close

#Add many of records:
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany('INSERT INTO customers VALUES (?,?,?)',(list))
    #Commit and close conection
    conn.commit()
    conn.close()

#Delete a record from Database
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute('DELETE from customers WHERE rowid = (?)', id)
#Commit our command and close
    conn.commit()
    conn.close

#Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute('SELECT * from customers WHERE email = (?)',(email,))

    items = c.fetchall()

    for item in items:
        print(item)
    
    conn.commit()
    conn.close()