import requests
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from bson.json_util import dumps
from extensions import mongo
from libs.strings import gettext
from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()


class Items(Resource):
    @classmethod
    def get(cls):
        products = mongo.db.products
        all = []
        for each in products.find():
            del(each['_id'])
            all.append(each)

        return all

    @classmethod
    def post(cls):
        """
        Add a list of Items
        :return:
        """
        # Get the product payload json
        data = request.get_json()

        # mongodb implementation
        products = mongo.db.products
        products.insert_many(data)
        return 'OK', 200
