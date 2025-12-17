from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, \
    logout_user, current_user, login_required
from werkzeug.utils import redirect
from datetime import datetime
from os import system

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    scans = db.relationship('NMap', backref='user', lazy=True)

class NMap(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    THMname = db.Column(db.String)
    date = db.Column(db.String)
    nmapStr = db.Column(db.String)
    fileRoute = db.Column(db.String)

with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = 'whatAnAmazingSecretKey!!'
login_manager = LoginManager(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(uid):
    user = User.query.get(uid)
    return user
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template("create.html")
    elif request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()

        if existing_user is not None:
            error = "That username is already taken"
            return render_template("create.html", error=error)
        else:
            user=User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect("/")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method== 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None:
            error="There is no User by that username!"
            return render_template("login.html", error=error)
        elif user.password == password:
            login_user(user)
            return redirect('/')
        else:
            error = "wrong password!"
            return render_template("login.html", error=error)
    else:
        return "Error"

@app.route('/nmapForm', methods=['GET','POST'])
@login_required
def nmap():
    if request.method=='GET':
        return render_template("nmapForm.html")
    elif request.method == 'POST':
        thmName = request.form['thmName']
        address = request.form['address']
        sv = request.form.get('sv', '')
        sc = request.form.get('sc', '')
        su = request.form.get('su', '')
        so = request.form.get('so', '')
        port = request.form.get('port', '')
        if port == '-p ':
            port += request.form['p_one_num']
        elif port == '-p':
            port += ' ' + request.form['p_rng_str'] + "-" + request.form['p_rng_end']
        t_speed = ''
        if '-T' in request.form:
            slider_val = request.form.get('t_num','')
            if slider_val:
                t_speed = f"-T{slider_val}"
        nmap_string = f"nmap {sv} {sc} {su} {so} {port} {t_speed} {address}"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        thmName = request.form['thmName']
        userName = current_user.username

        fileName = f"static/{userName}{timestamp}.txt"

        print(fileName)
        print(thmName)

        fullString = f"{nmap_string} -oN {fileName}"

        system(fullString)
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nmap = NMap(THMname=thmName, date = date, nmapStr=nmap_string,fileRoute=fileName, user_id=current_user)
        db.session.add(nmap)
        db.session.commit()

        return render_template("nmapForm.html", nmap = nmap_string)


@app.route("/view")
@login_required
def view():
    nmaps = NMap.query.filter_by(user_id=current_user.id).all()
    results = []
    for i in nmaps:
        filepath = i.fileRoute
        with open(filepath, "r") as f:
            results.append(f.read())

    return render_template("view.html", nmaps=nmaps, results=results)

@app.errorhandler(404)
def e404(err):
    return render_template("error404.html")

@app.errorhandler(401)
def e401(err):
    return render_template("error401.html")

@app.errorhandler(500)
def e500(err):
    return render_template("error500.html")

app.run(debug=True)