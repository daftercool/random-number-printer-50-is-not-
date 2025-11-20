import sqlite3

connection = sqlite3.connect ("salim.db")
cursor = connection.cursor()
cursor.execute("""
              CREATE TABLE  IF NOT EXISTS workers (
               
               id INTEGER PRIMARY KEY,
               NAME TEXT,
               DATE TEXT 
                )
               """)
               
     
               
              
              

connection.commit()
connection.close()

               