from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

mongo = PyMongo()
db = SQLAlchemy()
ma = Marshmallow()
