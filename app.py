from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "random string"
app.config['UPLOAD_FOLDER'] = 'templates'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    mail = db.Column(db.String(100)) 
    msg = db.Column(db.String(500))

    def __init__(self, name, mail, msg) -> None:
        self.name = name
        self.mail = mail
        self.msg = msg

@app.route('/', methods=['GET', 'POST'])
def index():
    photos = list(set(os.listdir('./static/images/photos/')))
    if request.method == 'POST':
        data = Data(request.form['name'], request.form['mail'], request.form['msg'])
        db.session.add(data)
        db.session.commit()
        return render_template('index.html', photos=photos, flag=True)
    return render_template('index.html', photos=photos, flag=False)

@app.route('/feed_data', methods=['GET', 'POST'])
def fetch():
    return render_template('data.html', data = Data.query.all())

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(full_path, filename)