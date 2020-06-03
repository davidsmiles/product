from flask import request
from flask_restful import Resource

from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()


class OrderItems(Resource):
    @classmethod
    def get(cls):
        """
        This Resource is only called from the Orders Service
        Receives a JSON data of item_ids and returns a list of the model of each item
        :return: list of item_model
        """
        data = request.get_json()

        items = []
        for _id in data['item_ids']:
            item = ItemModel.find_by_id(_id)
            if not item:
                continue

            items.append(item)

        return item_schema.dump(items, many=True)
