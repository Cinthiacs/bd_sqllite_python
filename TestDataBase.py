import sqlite3
import csv

#Conect to a database
conn = sqlite3.connect('customer.db')

#Create a cursor

c = conn.cursor()

#Create a Table

#c.execute('''CREATE TABLE customers(
 #         first_name TEXT,
 #         last_name TEXT,
 #         email TEXT
#)''')

#DataTypes:
#Null
#Integer
#Real
#Text
#Blob

#many_customer = [
#    ('Cinthia','Cavalheiro','cinthiadiascavalheiro@gmail.com'),
#    ('Gustavo','Cavalheiro','gustavo@gmail.com'),
#    ('Angela','Dias Cavalheiro','angeladiascavalheiro@gmail.com')
#]

#c.executemany("INSERT INTO customers VALUES(?,?,?)",many_customer)

#Query the Database
#c.execute("SELECT * FROM customers")

#Search for especific things
#c.execute("SELECT * FROM  customers WHERE last_name = 'Cavalheiro'")

#Starts with Ca and ends with whatever

#c.execute("SELECT * FROM  customers WHERE last_name LIKE 'Ca%'")

c.execute("SELECT * FROM  customers WHERE email LIKE '%gmail.com'")

#Select the rows:
#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

items = c.fetchall()

print('Name:' + '\t\t     Email:')
print('-----' + '\t\t     --------')
for i in items:
    print (i[0] + ' ' + i[1] + '\t\t ' + i[2])
    #print(i)
    #print(i[0])

print('Command excecuted succesfully')
#Commit the command
conn.commit()

#Close the connection
conn.close()

