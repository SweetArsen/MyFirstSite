from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    apart_num = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Article %r>' %self.id




@app.route("/")
def index():
    return render_template("base.html")

@app.route("/about")
def about ():
    return render_template("About.html")

@app.route("/pm")
def pay_ment ():
    return render_template("Payment.html")

@app.route("/docs")
def docs_and_otch():
    return render_template("docs.html")

@app.route("/aplc")
def aplications():
    return render_template("aplications.html")

@app.route("/reg")
def registration():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)