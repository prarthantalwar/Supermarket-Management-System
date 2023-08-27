import mysql.connector as sqlc
from dotenv import load_dotenv
load_dotenv()
import os

# COMMAND TO CONNECT THE DATABASE
myconn=sqlc.connect(host=os.getenv('db_host'), user=os.getenv('db_user'), password=os.getenv('db_password'),db=os.getenv('db_name'))

# COMMAND TO CREATE A CURSOR
mycursor=myconn.cursor()

# COMMAND TO CREATE DATABASE (ALREADY EXECUTED IN THE MYSQL SHELL)
#mycursor.execute("CREATE DATABASE BILLING_SYSTEM")

# COMMAND TO USE THE CREATED DATABASE
mycursor.execute("USE talwar_supermarket_management_system")

#mycursor.execute("SELECT EXISTS(SELECT * from USERS WHERE USERNAME='admin' AND PASS='administrat' )")
# mycursor.execute("SELECT USER_ROLE FROM USERS")

# data=mycursor.fetchall()
# for i in data:
#     if i[0] == "Data Operator":
#         print(i[0])
