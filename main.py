from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

#Create the Database in mysql
DB_NAME = "sample"
DB_USERNAME = "root"
DB_PASSWD = "admin123"
DB_HOST = "localhost"
DB_CREATE_COMMAND = "mysql://{}:{}@{}".format(DB_USERNAME, DB_PASSWD, DB_HOST)
DB_URI = DB_CREATE_COMMAND + "/" + DB_NAME

engine = sqlalchemy.create_engine(DB_CREATE_COMMAND) 
engine.execute("CREATE DATABASE IF NOT EXISTS " + DB_NAME) #create db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "({}: {})".format(self.user_id, self.user_name)

    def to_dict(self):
        return { "user_name": self.user_name }


@app.route("/users")
def home():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

if __name__ == "__main__":
    app.run(debug=True)
    




