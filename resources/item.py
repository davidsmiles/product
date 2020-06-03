from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from libs.strings import gettext
from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()


class Item(Resource):
    @classmethod
    def get(cls, item_id):
        item = ItemModel.find_by_id(item_id)
        if not item:
            return gettext("item_not_exist"), 404

        return item_schema.dump(item)

    @classmethod
    def put(cls, item_id):
        # Get the product payload json
        data = request.get_json()

        # Check if exists
        item = ItemModel.find_by_id(item_id)

        if not item:
            return {
                'message': gettext("item_not_exist").format(item_id),
                'code': 404
            }, 404

        item.update(data)
        return {}, 200

    @classmethod
    def delete(cls, item_id):
        # Check if exists
        item = ItemModel.find_by_id(item_id)

        if not item:
            return {
                'message': gettext("item_not_exist").format(item_id),
                'code': 404
            }, 404

        item.delete()
        return {}, 204