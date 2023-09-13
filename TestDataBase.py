import sqlite3
import csv

#Conect to a database
conn = sqlite3.connect('customer.db')

#Create a cursor

c = conn.cursor()

#Create a Table

#c.execute('''CREATE TABLE customers(
#          first_name TEXT,
#          last_name TEXT,
#          email TEXT
#)''')

#DataTypes:
#Null
#Integer for int numbers
#Real for float numbers
#Text for strings
#Blob for images

#many_customer = [
#    ('Cinthia','Cavalheiro','cinthiadiascavalheiro@gmail.com'),
#    ('Gustavo','Cavalheiro','gustavo@gmail.com'),
#    ('Angela','Dias Cavalheiro','angeladiascavalheiro@gmail.com')
#]

#Query the Database with all information
#c.executemany("INSERT INTO customers VALUES(?,?,?)",many_customer)


#Query the DataBase with LIMIT:
#c.execute('SELECT rowid, *FROM customers LIMIT 2')

#Query the DataBase with DESCENDING:
#c.execute('SELECT rowid, *FROM customers ORDER BY rowid DESC LIMIT 2')

#Query the Database - AND/OR
#For And both have to be True 
#c.execute('SELECT rowid, * FROM customers WHERE last_name LIKE "Ca%" AND rowid = 2')

#For OR doesn´t both have to be True, just only one has to be.
#c.execute('SELECT rowid, * FROM customers WHERE last_name LIKE "Ca%" AND rowid = 2')

#Query the Database - ORDER BY like A to Z
#c.execute("SELECT rowid,*FROM customers ORDER BY first_name")


#Query the Database - ORDER BY
c.execute("SELECT rowid,*FROM customers ORDER BY rowid")

##Query the Database- ROW ID starts with 1

#c.execute('''UPDATE customers SET first_name = 'John' 
#         WHERE rowid = 1''')    

#Commit the command
conn.commit()

#Query the Database with a rowid
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()    

for item in items:
    print(item)

#Search for especific things
#c.execute("SELECT * FROM  customers WHERE last_name = 'Cavalheiro'")

#Starts with Ca and ends with whatever

#c.execute("SELECT * FROM  customers WHERE last_name LIKE 'Ca%'")

#c.execute("SELECT * FROM  customers WHERE email LIKE '%gmail.com'")

#Select the rows:
#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

#items = c.fetchall()

#print('Name:' + '\t\t     Email:')
#print('-----' + '\t\t     --------')
#for i in items:
#    print (i[0] + ' ' + i[1] + '\t\t ' + i[2])
    #print(i)
    #print(i[0])

print('Command excecuted succesfully')

#Close the connection
conn.close()