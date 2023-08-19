from flask import Flask, render_template,redirect, request
from database import mycursor

# COMMAND TO USE THE CREATED DATABASE
mycursor.execute("USE talwar_supermarket_management_system")

app = Flask(__name__)

@app.route("/")
def landing():
     return render_template('landing.html')



@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(type(username), username, type(password), password)

        query= f"SELECT EXISTS(SELECT * from USERS WHERE USERNAME='{username}' AND PASS='{password}')"
        mycursor.execute(query)
        data = mycursor.fetchall()
        response = data[0][0]
        if response == 1:
            query=f"SELECT USER_ROLE FROM USERS WHERE USERNAME='{username}'"
            print(query)
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data,type(data))
            response = data[0][0]
            print(response, type(response))
            if response == 'Administrator':
                return redirect("/admin")
            elif response == 'Data Operator':
                return redirect("/dataop")
            else:
                return redirect("/billop")
    return render_template('login.html')


@app.route("/logout")
def logout():
     return render_template('logout.html')




@app.route('/<string:page_name>')
def page(page_name="/"):
     try:
         return render_template(page_name+".html")
     except:
         return redirect("/")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)