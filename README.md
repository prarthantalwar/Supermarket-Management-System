# Supermarket-Management-System
Supermarket Management System

Used planetscale.com for online MySQL database

Used mysql workbench for connecting the database


password: main-2023-08-09-qlauah


Branch	main
Role	Admin
Username	1sp07eu0hq019gz3miv5

Password	pscale_pw_gTarXd9nbtPUS6nREhGxKAxkJwnAYmmfZ4032ryOCBj




.env

HOST=aws.connect.psdb.cloud
USERNAME=1sp07eu0hq019gz3miv5
PASSWORD=pscale_pw_gTarXd9nbtPUS6nREhGxKAxkJwnAYmmfZ4032ryOCBj
DATABASE=talwar-supermarket-management-system



main.py

from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

connection = MySQLdb.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl      = {
    "ca": "/etc/ssl/cert.pem"
  }
)




terminal

pip install python-dotenv mysqlclient