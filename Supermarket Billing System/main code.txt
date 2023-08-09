import mysql.connector as sqlc
import datetime
import time
import pyfiglet
import shutil

# COMMAND TO CONNECT THE DATABASE
myconn=sqlc.connect(host="localhost",user="root",password="Admin@123",db='Billing_System')
'''Write the corresponding user and password'''

# COMMAND TO CREATE A CURSOR
mycursor=myconn.cursor()

# COMMAND TO CREATE DATABASE (ALREADY EXECUTED IN THE MYSQL SHELL)
#mycursor.execute("CREATE DATABASE BILLING_SYSTEM")

# COMMAND TO USE THE CREATED DATABASE
mycursor.execute("USE BILLING_SYSTEM")

# COMMAND TO CREATE TABLES (ALREADY EXECUTED IN THE SHELL)
#mycursor.execute("CREATE TABLE PRODUCTS_INFO(PRODUCT_NAME VARCHAR(10) NOT NULL,PRODUCT_CODE VARCHAR(5) NOT NULL ,PRODUCT_TYPE VARCHAR(10) NOT NULL,PRODUCT_PRICE INT(6) NOT NULL,PRODUCT_EXPIRY_DATE DATE,PRODUCT_QUANTITY INT(5) NOT NULL,SUPPLIER_NAME VARCHAR(15) NOT NULL,SUPPLIER_CODE VARCHAR(5) NOT NULL,SUPPLIER_CONTACT BIGINT(10) NOT NULL)")

    
# To print the title
def print_big_text(text):
    result = pyfiglet.figlet_format(text, font = "big")
    lines = result.split("\n")
    terminal_rows, terminal_columns = shutil.get_terminal_size()
    for line in lines:
        number_of_spaces = terminal_columns - len(line)
        print(" " * number_of_spaces + line)

def admin_mod():
    # Administrator module
    print("\n\n\t\tSelect the module you want to access\t\t")
    print("\n")
    print("MODULE1:ADD PRODUCTS TO THE INVENTORY ")
    print("MODULE2:REPORT OF PRODUCTS IN STOCK ")
    print("MODULE3:SEARCH FOR A PARTICULAR PRODUCT FROM EXISTING TABLE OF RECORDS")
    print("MODULE4:EDIT PRODUCT DETAILS")
    print("MODULE5:APPLY DISCOUNTS ON PRODUCTS")
    print("MODULE6:REPORT OF PRODUCTS EXPIRING WITHIN 30 days")
    print("MODULE7:REPORT OF PRODUCTS REQUIRED")
    print("MODULE8:DELETE A RECORD FROM EXISTING TABLE")
    print("MODULE9:CALCULATE AND PRINT THE BILL")
    print("\n")
    module_number_to_access=int(input("ENTER THE MODULE NUMBER YOU WANT TO ACCESS(1,2,3,4,5,6,7,8,9) : "))
    print("\n")
    if module_number_to_access==1:
        module2()
    elif module_number_to_access==2:
        module10()
    elif module_number_to_access==3:
        module3()
    elif module_number_to_access==4:
        module4()
    elif module_number_to_access==5:
        module5()
    elif module_number_to_access==6:
        module6()
    elif module_number_to_access==7:
        module7()
    elif module_number_to_access==8:
        module9()
    elif module_number_to_access==9:
        module8()
    else:
        print("THIS IS AN INAPPROPRIATE MODULE NUMBER AND DOES NOT EXIST")
        print("\n")
        
def data_op():
    # Data operator module
    print("\n\t\tSelect the module you want to access\t\t")
    print("\n")
    print("MODULE1:ADD PRODUCTS TO THE INVENTORY")
    print("MODULE2:REPORT OF PRODUCTS IN STOCK")
    print("MODULE3:SEARCH FOR A PARTICUALR PRODUCT FROM EXISTING TABLE OF RECORDS")
    print("MODULE4:EDIT PRODUCT DETAILS")
    print("MODULE5:REPORT OF PRODUCTS EXPIRING WITHIN 30 days")
    print("MODULE6:REPORT OF PRODUCTS REQUIRED")
    print("MODULE7:DELETE A RECORD FROM EXISTING TABLE")
    print("\n")
    module_number_to_access=int(input("ENTER THE MODULE NUMBER TO ACCESS(1,2,3,4,5) : "))
    print("\n")
    if module_number_to_access==1:
        module2()
    elif module_number_to_access==2:
        module10()
    elif module_number_to_access==3:
        module3()
    elif module_number_to_access==4:
        module4()
    elif module_number_to_access==5:
        module6()
    elif module_number_to_access==6:
        module7()
    elif module_number_to_access==7:
        module9()
    else:
        print("THIS IS AN INAPPROPRIATE MODULE NUMBER OR IS NOT VALID")
        
def bill_op():
    # Bill operator module
    print("\n\t\tSelect the module you want to access\t\t")
    print("\n")
    print("MODULE1:SEARCH FOR A PARTICULAR PRODUCT FROM EXISTIMG TABLE OF RECORDS ")
    print("MODULE2:REPORT OF PRODUCTS IN STOCK")
    print("MODULE3:CALCULATE AND PRINT THE BILL")
    print("\n")
    module_number_to_access=int(input("ENTER THE MODULE NUMBER TO ACCESS(1,2,3) : "))
    print("\n")
    if module_number_to_access==1:
        module3()
    elif module_number_to_access==2:
        module10()
    elif module_number_to_access==3:
        module8()
    else:
        print("THIS IS AN INAPPROPRIATE MODULE NUMBER OR IS NOT VALID")
        
def table_print(data):
    #PRINTING OF TABLE
    print("\n")
    print(("-")*155)
    print("||  PROD NAME    ||  PROD CODE    ||   PROD TYPE   ||     PRICE     ||   EXP DATE    ||      QTY      ||    SUP NAME   ||  SUP CODE     ||   SUP PHONE   ||")
    print(("-")*155)
    for i in data :
        a=i[0]
        la=len(str(a))
        b=i[1]
        lb=len(str(b))
        c=i[2]
        lc=len(str(c))
        d=i[3]
        ld=len(str(d))
        e=i[4]
        le=len(str(e))
        f=i[5]
        lf=len(str(f))
        g=i[6]
        lg=len(str(g))
        h=i[7]
        lh=len(str(h))
        j=i[8]
        lj=len(str(j))
        space=chr(32)
        row="|| "+str(a)+space*(14-la)+"|| "+str(b)+space*(14-lb)+"|| "+str(c)+space*(14-lc)+"|| "+str(d)+space*(14-ld)+"|| "+str(e)+space*(14-le)+"|| "+str(f)+space*(14-lf)+"|| "+str(g)+space*(14-lg)+"|| "+str(h)+space*(14-lh)+"|| "+str(j)+space*(14-lj)+"||"
        print(row)
        print(("-")*155)
    print("\n")
    print("DATA RETRIEVED SUCCESSFULLY\n\n")
    
def module1():
    #LOGIN
    print("\n")
    print("\n\t\t ***** LOGIN *****")
    print("\n\t\t ", chr(32)*42)
    
def module2():
    #ADD PRODUCTS TO THE INVENTORY
    print("ADD PRODUCTS TO THE INVENTORY\n\n")
    print("Enter the details of the products : ")
    print("\n")
    print("\n")
    while True:
        print("\t\t\n\t\t") 
        #ENTER THE PRODUCT NAME
        product_name=input("Enter the product name (str): ")
        print("\n")
        #ENTER THE PRODUCT CODE
        product_code=input("Enter the product code (str): ")
        print("\n")
        #ENTER THE PRODUCT TYPE
        product_type=input("Enter the product type (str): ")
        print("\n")
        #ENTER THE PRODUCT PRICE
        product_price=int(input("Enter the product price (int): "))
        print("\n")
        #ENTER THE DATE OF PRODUCT EXPIRY
        product_expiry_date=input("Enter the date of product expiry (yyyy-mm-dd): ")
        print("\n")
        #ENTER THE PRODUCT QUANTITY
        product_quantity=int(input("Enter the product quantity (int): "))
        print("\n")
        #ENTER THE SUPPLER NAME 
        supplier_name=input("Enter the supplier name (str): ")
        print("\n")
        #ENTER THE SUPPLER CODE 
        supplier_code=input("Enter the supplier code (str): ")
        print("\n")
        #ENTER THE SUPPLER  CONTACT
        supplier_contact=int(input("Enter the supplier contact (int): "))
        print("\n")
        #COMMAND TO INSERT INTO TABLE
        mycursor.execute("INSERT INTO PRODUCTS_INFO VALUES('{}','{}','{}',{},'{}',{},'{}','{}',{})".format(product_name,product_code,product_type,product_price,product_expiry_date,product_quantity,supplier_name,supplier_code,supplier_contact))
        myconn.commit()
        print("\n")
        ch=input("Do you want to enter more(Y/N) :")
        if ch.upper()=="Y":
            continue
        else:
            print("\n")
            print("DATA INSERTED SUCCESSFULLY")
            break
        
def module3():
    #SEARCH FOR A PARTICULAR PRODUCT FROM EXISTING TABLE OF RECORDS!!!!!!!
    print("SEARCH FOR A PARTICULAR PRODUCT FROM EXISTING TABLE OF RECORDS")
    print("\n")
    print("\n")
    while True:
        print("\n")
        #ENTER THE PRODUCT CODE
        product_code=input("Enter the product code (str): ")
        print("\n")
        #ENTER THE PRODUCT TYPE
        product_type=input("Enter the product type  (str): ")
        print("\n")
        #COMMAND TO RETRIEVE
        mycursor.execute("SELECT * FROM PRODUCTS_INFO WHERE product_code='{}' and product_type='{}'".format(product_code,product_type))
        #COMMAND TO FETCH THE INFORMATION
        data=mycursor.fetchall()
        #PRINTING OF TABLE
        table_print(data)
        print("\n")
        ch=input("Do you want to search more(Y/N) :")
        if ch.upper()=="Y":
            continue
        else:
            print("\n")
            print("DATA RETRIEVED SUCCESSFULLY\n\n")
            break
        
def module4():
    #EDIT PRODUCT DETAILS
    print("EDIT PRODUCT DETAILS")
    print("\n")
    print("\n")
    while True:
        print("\n")
        #ENTER THE PRODUCT CODE WHOSE DETAILS HAS TO BE EDITED
        product_code=input("Enter the product code whose details has to be edited (str): ")
        print("\n")
        #ENTER THE PRODUCT NAME
        product_name=input("Enter the product name (str): ")
        print("\n")
        #ENTER THE PRODUCT TYPE
        product_type=input("Enter the product type (str): ")
        print("\n")
        #ENTER THE PRODUCT PRICE
        product_price=int(input("Enter the product price (int): "))
        print("\n")
        #ENTER TEH DATE OF PRODUCT EXPIRY
        product_expiry_date=input("Enter the date of product expiry (yyyy-mm-dd): ")
        print("\n")
        #ENTER THE PRODUCT QUANTITY
        product_quantity=int(input("Enter the product quantity (int): "))
        print("\n")
        #ENTER THE SUPPLIER NAME
        supplier_name=input("Enter the supplier name (str): ")
        print("\n")
        #ENTER THE SUPPLIER CODE 
        supplier_code=input("Enter the supplier code (str): ")
        print("\n")
        #ENTER THE SUPPLIER CONTACT
        supplier_contact=int(input("Enter the supplier contact (int): "))
        print("\n")
        #COMMAND TO UPDATE
        mycursor.execute("UPDATE PRODUCTS_INFO SET product_name='{}',product_type='{}',product_price={},product_expiry_date='{}',product_quantity={},supplier_name='{}',supplier_code='{}',supplier_contact={} WHERE product_code='{}'".format(product_name,product_type,product_price,product_expiry_date,product_quantity,supplier_name,supplier_code,supplier_contact,product_code))    
        myconn.commit()
        print("\n")
        ch=input("Do you want to edit more(Y/N) :")
        if ch.upper()=="Y":
            continue
        else:
            print("\n")
            print("DATA UPDATED SUCCESSFULLY\n\n")
            break
        
def module5():
    #APPLY DISCOUNTS
    print("APPLY DISCOUNTS")
    print("\n")
    print("\n")
    while True:
        #ENTER THE DISCOUNT
        disc=int(input("Enter the discount to be applied (between 0 and 1): "))
        #ENTER THE PRODUCT CODE
        product_code=input("Enter the product code(str): ")
        print("\n")
        #ENTER THE PRODUCT TYPE 
        product_type=input("Enter the product type(str): ")
        print("\n")
        #COMMAND TO UPDATE
        mycursor.execute("UPDATE PRODUCTS_INFO SET product_price=product_price*(1-{}) WHERE product_code='{}' and product_type='{}'".format(disc,product_code,product_type))
        myconn.commit()
        print("\n")
        ch=input("Do you want to apply more(Y/N) :")
        if ch.upper()=="Y":
            continue
        else:
            print("\n")
            print("DISCOUNT APPLIED SUCCESSFULLY\n\n")
        
def module6():
    #REPORT OF PRODUCTS EXPIRING WITHIN 30 days
    print("REPORT OF PRODUCTS EXPIRING WITHIN 30 DAYS")
    print("\n")
    print("\n")
    today=datetime.date.today()
    next_month_date=days_after = (datetime.date.today()+datetime.timedelta(days=30)).isoformat()
    #COMMAND TO RETRIEVE
    mycursor.execute("SELECT * FROM PRODUCTS_INFO WHERE product_expiry_date between '{}' and '{}'".format(today,next_month_date))
    data=mycursor.fetchall()
    #PRINTING OF TABLE
    table_print(data)
    
def module7():
    #REPORT OF PRODUCTS REQUIRED
    print("REPORT OF PRODUCTS REQUIRED")
    print("\n")
    print("\n")
    #COMMAND TO RETRIEVE DATA
    mycursor.execute("SELECT * FROM PRODUCTS_INFO WHERE product_quantity<50")
    data=mycursor.fetchall()
    #PRINTING OF TABLE
    table_print(data)
    print("\n")
    
def module8():
    print(" CALCULATE AND PRINT THE BILL")
    print("\n")
    print("\n")
    #CREATING A TABLE FOR BILL
    mycursor.execute("CREATE TABLE BILL(SL_NO INT(5), ITEM VARCHAR(10) NOT NULL, QTY INT(5) NOT NULL, RATE INT(5) NOT NULL, AMOUNT INT(10))")
    #ENTER THE CUSTOMER NAME
    customer_name=input("Enter the customer name : ")
    print("\n")
    #ENTER THE CUSTOMER'S PHONE NUMBER 
    phone_no=int(input("Enter the customer's phone number : "))
    print("\n")
    n=0
    x=datetime.date.today()
    print("\n")
    v=time.time()
    y=time.ctime(v)
    print("\n")
    total_price=total_bill_amount=total_amount=0
    print("\n")
    while True:
        #ENTER THE PRODUCT CODE
        product_code=input("Enter the product code : ")
        print("\n")
        #QUANTITY OF THE PRODUCT AVAILABLE
        mycursor.execute("SELECT PRODUCT_QUANTITY FROM PRODUCTS_INFO WHERE PRODUCT_CODE = '{}'".format(product_code))
        e=mycursor.fetchall()
        qty_avail=e[0][0]
        print("\n")
        #ENTER THE NUMBER OF UNITS YOU WANT TO PURCHASE
        print("\nIf the customer wants to know the total number of units, let them know that there are", qty_avail, "units available in total including the number of units in their basket if present")
        qty=int(input("\nEnter the number of units customer wants to purchase: "))
        print("\n")
        #PRICE OF THE PRODUCT
        mycursor.execute("SELECT PRODUCT_PRICE FROM PRODUCTS_INFO WHERE PRODUCT_CODE = '{}'".format(product_code))
        e1=mycursor.fetchall()
        price=e1[0][0]
        print("\n")
        #NAME OF THE PRODUCT
        mycursor.execute("SELECT PRODUCT_NAME FROM PRODUCTS_INFO WHERE PRODUCT_CODE = '{}'".format(product_code))
        e2=mycursor.fetchall()
        item=e2[0][0]
        print("\n")
        amount=qty*price
        qty_left=qty_avail-qty
        n=n+1
        #COMMAND TO UPDATE
        if qty_left<=0:
            mycursor.execute("DELETE FROM PRODUCTS_INFO WHERE PRODUCT_CODE = '{}'".format(product_code))
            myconn.commit()
        else:
            mycursor.execute("UPDATE PRODUCTS_INFO SET product_quantity={} WHERE PRODUCT_CODE = '{}'".format(qty_left,product_code))
            myconn.commit()
        mycursor.execute("INSERT INTO BILL SET SL_NO = {}, ITEM = '{}', QTY = {}, RATE = {}, AMOUNT = {}".format(n,item,qty,price,amount))
        myconn.commit()
        ch=input("Buy more products ?(Y/N) :")
        print("\n\n")
        if ch.upper()=="Y":
            continue
        else:
            print("\n")
            break
    print("\n")
    print(("=")*188)
    print("\n")
    print("\t\t\t\t\t\t","   CASH RECEIPT")
    print("\t\t\t\t\t\t   ","-"*12)
    print("\n")
    print("\t\t\t CUSTOMER NAME: ",customer_name,"\t\t\t","Phone number: ",phone_no)
    print("\t\t\t DATE: ",x,"\t\t\t","TIME: ",y)
    print("\n")
    #PRINTING OF BILL
    print("\n")
    print("\t\t\t",("-")*75)
    print("\t\t\t","|| Sl. No. ||    ITEM          ||   QTY   ||     RATE     ||   AMOUNT    ||")
    print("\t\t\t",("-")*75)
    #COMMAND TO RETRIEVE DATA
    mycursor.execute("SELECT * FROM BILL")
    data=mycursor.fetchall()
    for i in data:
        a=i[0]
        la = len(str(a))
        b=i[1]
        lb = len(str(b))
        c=i[2]
        lc = len(str(c))
        d=i[3]
        ld = len(str(d))
        e=i[4]
        le = len(str(e))
        space = chr(32)
        row="\t\t\t "+"|| "+str(a)+space*(8-la)+"|| "+str(b)+space*(17-lb)+"|| "+str(c)+space*(8-lc)+"|| "+str(d)+space*(13-ld)+"|| "+str(e)+space*(12-le)+"||"
        print(row)
    print("\t\t\t",("-")*75)
    print("\n")
    #COMMAND TO GET TOTAL
    mycursor.execute("SELECT SUM(AMOUNT) FROM BILL")
    item_total=mycursor.fetchall()
    total_amount=int(item_total[0][0])
    print("\t\t\t CGST @5% = ", round(total_amount*0.05))
    print("\t\t\t SGST @5% = ", round(total_amount*0.05))
    print("\t"*10," GRAND TOTAL=",total_amount+(total_amount)*0.1)
    print("\n")
    print("\n\t\t\t\t\t\tTHANK YOU VISIT AGAIN \n")
    print("\t\t\t\t  SUPERMART,2ND CROSS ROAD,LADYHILL,MANAGALURU,KARNATAKA-575003\n\n\n\n")
    print(("=")*188)
    print("\n")
    # DROP THE TABLE BILL 
    mycursor.execute("DROP TABLE BILL")
    myconn.commit()

def module9():
    #DELETE A RECORD FROM EXISTING TABLE
    print("DELETE A RECORD FROM EXISTING TABLE")
    print("\n")
    print("\n")
    while True:
        #ENTER THE PRODUCT CODE 
        product_code=input("Enter the product code :")
        print("\n")
        #DO YOU REALLY WANT TO DELETE THE RECORD
        choice1=input("Delete the record (y/n): ")
        if choice1.lower()=="y":
            choice2=input("CONFIRM DELETION (y/n): ")
            if choice2.lower()=="y":
                #COMMANDS TO DELETE
                mycursor.execute("DELETE FROM PRODUCTS_INFO WHERE product_code={}".format(product_code))
                myconn.commit()
                print("RECORD DELETED SUCCESSFULLY")
            else:
                print("No record was deleted")
        else:
            print("No record was deleted")
        print("\n")
        print("\n")
        ch=input("Do you want to delete more(Y/N) :")
        if ch.upper()=="Y":
            continue
        else:
            break
    
def module10():
    #REPORT OF PRODUCTS IN STOCK
    print("REPORT OF PRODUCTS IN STOCK:")
    mycursor.execute("SELECT * FROM PRODUCTS_INFO")
    #FETCH DATA FROM TABLE
    data=mycursor.fetchall()
    table_print(data)
    
#MAIN
while True:
    print("\n")
    print(("-")*188)
    print_big_text(" SUPERMARKET BILLING SYSTEM ")
    print("\n")
    print(("=")*188)
    print("\n")
    module1()
    #ENTER YOUR USERNAME 
    user_id=input("Enter your username : ")
    print("\n")
    if user_id.lower()=="admin":
        e=0
        c=3
        print("\n")
        while True :
            #ENTER YOUR PASSWORD
            password=input("Enter your password : ")
            if password.lower()=="administrator":
                while True:
                    admin_mod()
                    print("Do you want to access other modules ?\n\n")
                    ch=input("If yes, enter \"Y\", else enter anything else :")
                    print("\n")
                    if ch.upper()=="Y":
                        continue
                    else:
                        print("\n\n\n\n\t\t\t********** THANK YOU ***********\n\n\n")
                        break
                break
            else:
                print("\n")
                print("The password you have entered is wrong, you have,",c,"chances left\n\n")
                print("\n")
                if c>0:
                    c=c-1
                    print("\n")
                    continue
                else:
                    c=c-1
                    print("You have used up all your chances, please login again or try again later\n\n")
                    e=1
                    break
                
        if e==1:
            print("\n\nDo you want to try logging in again ?\n")
            ch=input("If yes, enter \"Y\", else enter anything else :")
            print("\n")
            if ch.upper()=="Y":
                continue
            else:
                print("\n\n\n\n\t\t\t********** THANK YOU ***********")
                break
        #break             #Uncomment this break if you don't want login right after Thank you
    elif user_id.lower()=="dataop":
        e=0
        c=3
        print("\n")
        while True :
            #ENTER YOUR PASSWORD
            password=input("Enter your password : ")
            if password.lower()=="dataoperator":
                while True:
                    data_op()
                    print("Do you want to access other modules ?\n\n")
                    ch=input("If yes, enter \"Y\", else enter anything else :")
                    print("\n")
                    if ch.upper()=="Y":
                        continue
                    else:
                        print("\n\n\n\n\t\t\t********** THANK YOU ***********\n\n\n")
                        break
                break
            else:
                print("\n")
                print("The password you have entered is wrong, you have,",c,"chances left\n\n")
                print("\n")
                if c>0:
                    c=c-1
                    print("\n")
                    continue
                else:
                    c=c-1
                    print("You have used up all your chances, please login again or try again later\n\n")
                    e=1
                    break
                
        if e==1:
            print("\n\nDo you want to try logging in again ?\n")
            ch=input("If yes, enter \"Y\", else enter anything else :")
            print("\n")
            if ch.upper()=="Y":
                continue
            else:
                print("\n\n\n\n\t\t\t********** THANK YOU ***********")
                break
        #break             #Uncomment this break if you don't want login right after Thank you
    elif user_id.lower()=="billop":
        e=0
        c=3
        print("\n")
        while True :
            #ENTER YOUR PASSWORD
            password=input("Enter your password : ")
            if password.lower()=="billoperator":
                while True:
                    bill_op()
                    print("Do you want to access other modules ?\n\n")
                    ch=input("If yes, enter \"Y\", else enter anything else :")
                    print("\n")
                    if ch.upper()=="Y":
                        continue
                    else:
                        print("\n\n\n\n\t\t\t********** THANK YOU ***********\n\n\n")
                        break
                break
            else:
                print("\n")
                print("The password you have entered is wrong, you have,",c,"chances left\n\n")
                print("\n")
                if c>0:
                    c=c-1
                    print("\n")
                    continue
                else:
                    c=c-1
                    print("You have used up all your chances, please login again or try again later\n\n")
                    e=1
                    break
                
        if e==1:
            print("\n\nDo you want to try logging in again ?\n")
            ch=input("If yes, enter \"Y\", else enter anything else :")
            print("\n")
            if ch.upper()=="Y":
                continue
            else:
                print("\n\n\n\n\t\t\t********** THANK YOU ***********")
                break
        #break             #Uncomment this break if you don't want login right after Thank you
    elif user_id.lower()=="term":
        print("\n\nPPROGRAM TERMINATED \n\n")
        print("\n\n\n\n\t\t\t********** THANK YOU ***********")
        break
    else:
        print("Sorry you have entered wrong credentials or are an inappropriate user\n\n")
        print("Do you want to try once more \n\n")
        ch=input("If yes, enter \"Y\", else enter anything else :")
        if ch.upper()=="Y":
            continue
        else:
            print("\n\n\n\n\t\t\t********** THANK YOU ***********")
            break
