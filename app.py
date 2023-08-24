from flask import Flask, render_template,redirect, request, session,g, flash
from database import mycursor
import os



# COMMAND TO USE THE CREATED DATABASE
mycursor.execute("USE talwar_supermarket_management_system")

app = Flask(__name__)

app.secret_key=os.urandom(33)

@app.route("/")
def landing():
     return render_template('landing.html')



@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)
        username = request.form['username']
        password = request.form['password']
        print(type(username), username, type(password), password)

        query= f"SELECT EXISTS(SELECT * from USERS WHERE USERNAME='{username}' AND PASS='{password}')"
        print("\n\n\n\n\n\n\n\n")
        print(query)
        print("\n\n\n\n\n\n\n\n")
        mycursor.execute(query)
        data = mycursor.fetchall()
        response = data[0][0]
        if response == 1:
            print('here')
            query=f"SELECT USER_ROLE FROM USERS WHERE USERNAME='{username}'"
            print(query)
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data,type(data))
            response = data[0][0]
            print(response, type(response))
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

@app.route('/user_deats')
def user_deats():
    if g.user:
        return render_template('user_deats.html', user=session['user'])
    return redirect('/')


@app.route('/cust_deats')
def cust_deats():
    if g.user:
        return render_template('cust_deats.html', user=session['user'])
    return redirect('/')


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


@app.route('/supp_deats')
def supp_deats():
    if g.user:
        return render_template('supp_deats.html', user=session['user'])
    return redirect('/')


@app.route('/search_prod_supp_deats')
def search_prod_supp_deats():
    if g.user:
        return render_template('search_prod_supp_deats.html', user=session['user'])
    return redirect('/')


@app.route('/del_prod')
def del_prod():
    if g.user:
        return render_template('del_prod.html', user=session['user'])
    return redirect('/')


@app.route('/prod_req')
def prod_req():
    if g.user:
        return render_template('prod_req.html', user=session['user'])
    return redirect('/')


@app.route('/prod_30_exp')
def prod_30_exp():
    if g.user:
        return render_template('prod_30_exp.html', user=session['user'])
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
        return render_template('list_prods.html', user=session['user'])
    return redirect('/')


@app.route('/add_prods')
def add_prods():
    if g.user:
        return render_template('add_prods.html', user=session['user'])
    return redirect('/')


@app.route('/apply_rem_disc')
def apply_rem_disc():
    if g.user:
        return render_template('apply_rem_disc.html', user=session['user'])
    return redirect('/')


@app.route('/bill')
def bill():
    if g.user:
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