from a.test import t 
import sqlite3
import os
from dotenv import load_dotenv 
load_dotenv()

DB_PATH = os.getenv('DB_PATH')
PLANINHA_PATH = os.getenv('PLANINHA_CLIENTES')
db = sqlite3.connect(DB_PATH)

cursor = db.cursor()

# Create a table
#It was already created
# cursor.execute("""
#         CREATE TABLE customers (
#             first_name TEXT,
#             last_name TEXT,
#             email TEXT)
#         """)

#Adding one entry
# cursor.execute("""
#                INSERT INTO customers VALUES ('Maria', 'Oliveire', 'js@email.com')
#                """)

#Adding many entries 
# many_customers = [
#         ("a","aa","aa@email.com"),
#         ("d","dd","dd@email.com"),
#         ("c","cc","cc@email.com"),
#         ("b","bb","bb@email.com"),
#         ]
#
# cursor.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)

# cursor.execute("SELECT * FROM customers")
# cursor.execute("SELECT * FROM customers")
# # print(cursor.fetchone())
# cursor.fetcmany(3)
#get the data of the last query execulted
# data = cursor.fetchall()
# print(data)

#Commit the comand
db.commit()
db.close()
