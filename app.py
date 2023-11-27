from flask import Flask, render_template
from sqlalchemy import create_engine
from models.models import *

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:edykab247@localhost/sti_data"
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    return 'Welcome!'

@app.route('/show_form')
def show_form():
    return render_template('forms.html')

if __name__ == '__main__':
    app.run(debug=True)
