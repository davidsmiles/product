import requests
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from libs.strings import gettext
from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()


class Items(Resource):
    @classmethod
    def get(cls):
        return item_schema.dump(ItemModel.find_all(), many=True)

    @classmethod
    def post(cls):
        """
        Add a list of Items
        :return:
        """
        # Get the product payload json
        data = request.get_json()

        """
            Use this implementation if application is a multi-store system

            store_id = get_jwt_identity()
            response = requests.get(f'http://nginx-service/stores/identify/{store_id}')

            if response.status_code == 200:
            # Check if exists
            for each_item in data:
                item = item_schema.load(each_item, partial=('store_id',))
                if ItemModel.find_by_name(item.name):
                    return gettext("item_already_exist"), 302

                item.store_id = response.json()['id']
                item.save_to_db()
            return 'OK', 200
        """
        for each_item in data:
            item = item_schema.load(each_item)
            if ItemModel.find_by_name(item.name):
                return gettext("item_already_exist"), 302

            item.save_to_db()
        return 'OK', 200
