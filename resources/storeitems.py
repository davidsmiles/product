import requests
from flask_restful import Resource

from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()


class StoreItems(Resource):
    @classmethod
    def get(cls, store_id):
        """
        Sends /GET request to STORE Service to Identify the Store
        and returns items of that store

        :param store_id: of Store
        :return: all Items of the Store whose STORE_ID was given
        """
        resp = requests.get(f'http://nginx-service/stores/identify/{store_id}')
        if resp.status_code == 200:
            _id = resp.json()['id']

            items = ItemModel.find_by_store_id(_id)
            return item_schema.dump(items, many=True), 200

        return "encountered a problem", 404
