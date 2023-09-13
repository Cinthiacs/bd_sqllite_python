import TestDataBase1

#Add a record to a DataBase
#TestDataBase1.add_one('Ana','Silva','ana.gmail.com')

#Add a bunch of records:


#Delete Record use rowid as string
#TestDataBase1.delete_one('1')
#TestDataBase1.delete_one('5')

#stuff = [
#    ('Julio','Oliveira','julio@gmail.com'),
#    ('Nicolas','Costa','nicolas@gmail')
#]

#TestDataBase1.add_many(stuff)
#Show all the records
#TestDataBase1.show_all()

TestDataBase1.email_lookup('gustavo@gmail.com')