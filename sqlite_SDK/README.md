#This is a very simple SDK over built-in Python sqlite3 library
 #to make your code readibility and supportability better
  #so that you will not have any raw sql queries inside your code.

#USAGE
Let's say you have a database folder where you have db.py file.

from database.db import Database  #importing the Database class from db.py

db = Database("database.db")   # creating an instance of our database class and giving him .db file

db.user_exixts() # for example will return True if the user is in the database

#END
