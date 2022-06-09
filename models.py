from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Plants(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    scientific_name = db.Column(db.String)
    is_poisonous = db.Column(db.Boolean, nullable=False)
    primary_color = db.Column(db.String)
