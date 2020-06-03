import os

from dotenv import load_dotenv

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from extensions import *
from libs.strings import set_default_locale

from resources.item import Item
from resources.items import Items
from resources.orderitems import OrderItems
from resources.storeitems import StoreItems

app = Flask(__name__)

load_dotenv('.env')
app.config.from_object(os.environ['APPLICATION_SETTINGS'])

# Api
api = Api(app)
jwt = JWTManager(app)


# in app use
db.init_app(app)
ma.init_app(app)
mongo.init_app(app)


@app.before_first_request
def create_all():
    db.create_all()


@app.route('/<name>')
def index(name):
   products = mongo.db.products
   products.insert({
       'name': name,
       'category': 'accessory',
       'price': 20
   })
   return 'Added an item!'


set_default_locale('en-us')
api.add_resource(Item, '/products/items/<int:item_id>')
api.add_resource(Items, '/products/items')
# api.add_resource(StoreItems, '/products/<string:store_id>/items') # multi-store system
api.add_resource(OrderItems, '/products/orders/items')


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    mongo.init_app(app)
    app.run(host='0.0.0.0')