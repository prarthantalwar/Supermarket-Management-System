from flask import Flask, render_template,redirect

app = Flask(__name__)

@app.route("/")
def landing():
     return render_template('landing.html')



@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # handle request
         pass
    return render_template('login.html')




@app.route('/<string:page_name>')
def page(page_name="/"):
     try:
         return render_template(page_name+".html")
     except:
         return redirect("/")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)