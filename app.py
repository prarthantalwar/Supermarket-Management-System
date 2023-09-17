import os
from flask import Flask, render_template,redirect, request, session, g, flash
from database import mycursor,myconn
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import pandas as pd
import datetime



# COMMAND TO USE THE CREATED DATABASE
mycursor.execute("USE talwar_supermarket_management_system")

app = Flask(__name__)

app.secret_key=os.urandom(33)
app.config['UPLOAD_FOLDER'] = 'static/uploaded_excel'



class Uploadexcel(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload Excel Sheet")




@app.route("/")
def landing():
     return render_template('landing.html')



@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)
        username = request.form['username']
        password = request.form['password']
        query= f"SELECT EXISTS(SELECT * from USERS WHERE USERNAME='{username}' AND PASS='{password}')"
        mycursor.execute(query)
        data = mycursor.fetchall()
        response = data[0][0]
        if response == 1:
            query=f"SELECT USER_ROLE FROM USERS WHERE USERNAME='{username}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            response = data[0][0]
            if response == 'Administrator':
                session['user'] = request.form['username']
                flash('You have successfully logged in',)
                return redirect("/admin")
            elif response == 'Data Operator':
                session['user'] = request.form['username']
                flash('You have successfully logged in')
                return redirect("/dataop")
            else:
                session['user'] = request.form['username']
                flash('You have successfully logged in')
                return redirect("/billop")
        else:
            return render_template('login.html', error="Invalid login or credentials mismatch")
    return render_template('login.html')



@app.route('/admin')
def admin():
    if g.user:
        return render_template('admin.html', user=session['user'])
    return redirect('/')

@app.route('/billop')
def billop():
    if g.user:
        return render_template('billop.html', user=session['user'])
    return redirect('/')


@app.route('/dataop')
def dataop():
    if g.user:
        return render_template('dataop.html', user=session['user'])
    return redirect('/')




# Modules 






# def create_dataframe(column_names, data):
#     # Create a dictionary where keys are column names and values are lists of data
#     # Example of a column_name list =['Customer name','Customer ID', 'Customer Phone', 'Customer mail']
#     data_dict = {column: [item[i] for item in data] for i, column in enumerate(column_names)}

#     # Create a DataFrame from the dictionary
#     df = pd.DataFrame(data_dict)

#     return df










@app.route('/user_deats')
def user_deats():
    if g.user:
        query = 'Select * from USERS'
        mycursor.execute(query)
        data=mycursor.fetchall()
        return render_template('user_deats.html', user=session['user'], data=data)
    return redirect('/')


@app.route('/cust_deats')
def cust_deats():
    if g.user:
        query = 'Select * from CUSTOMERS_INFO'
        mycursor.execute(query)
        data=mycursor.fetchall()
        print(data)


        # Add functionality to download in excel and pdf 


        
        # query2 = "SELECT column_name FROM information_schema.columns WHERE table_name = 'USERS'"
        # mycursor.execute(query2)
        # columns=mycursor.fetchall()
        # print(columns)
        return render_template('cust_deats.html', user=session['user'], data=data)
    return redirect('/')


@app.route('/supp_deats')
def supp_deats():
    if g.user:
        query = 'Select * from SUPPLIER_DETAILS'
        mycursor.execute(query)
        data=mycursor.fetchall()
        return render_template('supp_deats.html', user=session['user'], data=data)
    


    # Add functionality to download in excel and pdf
    return redirect('/')


@app.route('/search_prod_supp_deats',methods=['GET', 'POST'])
def search_prod_supp_deats():
    if g.user:
        if request.method == 'POST':
            prod_name = request.form['prod_name']
            prod_name_2= "%"+prod_name+"%"
            print(prod_name_2)
            query = f'Select SUPPLIER_ID from PRODUCTS_SUPPLIED where PRODUCT_NAME LIKE "{prod_name_2}"'
            print(query)
            mycursor.execute(query)
            data=mycursor.fetchall()
            supp_id=data[0][0]
            query2=f'SELECT * FROM SUPPLIER_DETAILS WHERE SUPPLIER_ID = {supp_id}'
            mycursor.execute(query2)
            data2=mycursor.fetchall()
            print(data2)
            return render_template('search_prod_supp_deats.html', user=session['user'], data=data2, prod_name=prod_name)
        return render_template('search_prod_supp_deats.html', user=session['user'])
    return redirect('/')


@app.route('/del_prod',methods=['GET', 'POST', 'DELETE'])
def del_prod():
    if g.user:
        if request.method == 'POST':
            bar_code = request.form['bar_code']
            query1=f'SELECT * FROM INVENTORY WHERE BARCODE ={bar_code}'
            mycursor.execute(query1)
            data=mycursor.fetchall()
            query = f'DELETE i1 FROM INVENTORY i1 JOIN (SELECT BARCODE FROM INVENTORY WHERE BARCODE = "{bar_code}") i2 ON i1.BARCODE = i2.BARCODE'
            mycursor.execute(query)
            myconn.commit()
            flash("Product Deleted Successfully")



            # Give an option to undo delete too 



            return render_template('del_prod.html', user=session['user'], data=data)
        return render_template('del_prod.html', user=session['user'])
    return redirect('/')


@app.route('/prod_req')
def prod_req():
    if g.user:
        mycursor.execute("SELECT * FROM INVENTORY WHERE QTY<50")
        data=mycursor.fetchall()
        col_heading = ["Sl. no.", "Product Name"]
        return render_template('prod_req.html', user=session['user'], data=data, col_heading = col_heading)
    return redirect('/')


@app.route('/prod_30_exp')
def prod_30_exp():
    if g.user:
        today=datetime.date.today()
        next_month_date = (datetime.date.today()+datetime.timedelta(days=30)).isoformat()
        #COMMAND TO RETRIEVE
        mycursor.execute("SELECT * FROM INVENTORY WHERE EXPIRY_DATE between '{}' and '{}'".format(today,next_month_date))
        data=mycursor.fetchall()
        col_heading = ["Sl. no.", "Product Name", "Barcode", "Quantity", "Expiry date"]
        return render_template('prod_30_exp.html', user=session['user'], data=data, col_heading = col_heading)
    return redirect('/')


@app.route('/edit_prod_deats')
def edit_prod_deats():
    if g.user:
        return render_template('edit_prod_deats.html', user=session['user'])
    return redirect('/')


@app.route('/search_prod_deats')
def search_prod_deats():
    if g.user:
        return render_template('search_prod_deats.html', user=session['user'])
    return redirect('/')


@app.route('/list_prods')
def list_prods():
    if g.user:
        query = 'Select * from INVENTORY'
        mycursor.execute(query)
        data=mycursor.fetchall()
        return render_template('list_prods.html', user=session['user'], data=data)
    return redirect('/')


@app.route('/add_prods', methods=['GET','POST'])
def add_prods():
    if g.user:
        print(g.user)
        if request.method=='POST':
            name = request.form['prod_name']
            barcode = request.form['barcode']
            mrp = request.form['mrp']
            rate = request.form['rate']
            qty = request.form['qty']
            expiry = request.form['expiry']
            query=f"INSERT INTO INVENTORY(PRODUCT_NAME, BARCODE, MRP, SELLING_PRICE, QTY, EXPIRY_DATE) VALUES('{name}','{barcode}','{mrp}','{rate}','{qty}','{expiry}')"
            mycursor.execute(query)
            myconn.commit()
            return redirect('/add_prods')

        return render_template('add_prods.html', user=session['user'])
    return redirect('/')


@app.route('/add_prod_by_excel', methods=['GET', 'POST'])
def add_prod_by_excel():
    if g.user:
        form = Uploadexcel()
        if form.validate_on_submit():
            file = form.file.data  # First grab the file
            upload_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'])

            # Ensure that the upload directory exists
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            # Check the file extension
            if file and allowed_file(file.filename):
                file_path = os.path.join(upload_dir, secure_filename(file.filename))
                file.save(file_path)  # Then save the file

                # Now, you can access and manipulate the uploaded Excel file using pandas
                df = pd.read_excel(file_path)

                # Perform your manipulations on the DataFrame here
                print(df.head())

                return redirect('/add_prods')
            else:
                flash('Invalid file format. Only Excel files (.xlsx, .xls) are allowed.', 'error')

        return render_template('add_prod_by_excel.html', user=session['user'], form=form)
    return redirect('/')

# Function to check if a file has an allowed extension
def allowed_file(filename):
    allowed_extensions = {'xlsx', 'xls'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions




@app.route('/todays_trans')
def todays_trans():
    if g.user:
        return render_template('todays_trans.html', user=session['user'])
    return redirect('/')


@app.route('/prod_supp_tod')
def prod_supp_tod():
    if g.user:
        return render_template('prod_supp_tod.html', user=session['user'])
    return redirect('/')



@app.route('/apply_rem_disc')
def apply_rem_disc():
    if g.user:
        return render_template('apply_rem_disc.html', user=session['user'])
    return redirect('/')


@app.route('/bill')
def bill():
    if g.user:
        print(g.user)
        return render_template('bill.html', user=session['user'])
    return redirect('/')







# @app.errorhandler(401)  # Error handler for unauthorized access to the page (login required).


@app.route("/logout")
def logout():
     session.pop('user', None)
     return render_template('logout.html')


@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user=session['user']



@app.route('/<string:page_name>')
def page(page_name="/"):
     try:
         return render_template(page_name+".html")
     except:
         return redirect("/")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)