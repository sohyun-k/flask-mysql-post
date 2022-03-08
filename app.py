import pymysql
from flask import Flask, render_template
from api import post
from db_connect import db

app = Flask(__name__)
app.register_blueprint(post)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@localhost:3306/elice_backend_pj_board"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template('mainPage.html')

if __name__ == '__main__':
    app.run()
