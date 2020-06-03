from flask_mongoengine import MongoEngine


db = MongoEngine()


def initialize_extensions(app):
    db.init_app(app)