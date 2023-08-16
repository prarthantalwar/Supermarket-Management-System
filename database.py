import mysql.connector as sqlc
from dotenv import load_dotenv
load_dotenv()
import os

# COMMAND TO CONNECT THE DATABASE
myconn=sqlc.connect(host=os.get_env(db_host), user=os.get_env(db_user), password=os.get_env(db_password),db=os.get_env(db_name))

# COMMAND TO CREATE A CURSOR
mycursor=myconn.cursor()

# COMMAND TO CREATE DATABASE (ALREADY EXECUTED IN THE MYSQL SHELL)
#mycursor.execute("CREATE DATABASE BILLING_SYSTEM")

# COMMAND TO USE THE CREATED DATABASE
mycursor.execute("USE talwar_supermarket_management_system")

mycursor.execute("SELECT * FROM INVENTORY;")

data=mycursor.fetchall()
print(data)