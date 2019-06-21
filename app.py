from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.secret_key='zelin'



@app.route('/',methods=['GET','POST'])
def index() :
    if request.method=='POST':
        cb_list=request.values.getlist("checkbox")

        if not all(cb_list):
            return 'Success'
        else:
            flash('illegal check item')
    return render_template('index.html')

if __name__ == '__main__' :
    app.run()
