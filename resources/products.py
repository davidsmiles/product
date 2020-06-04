import requests
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from mongoengine.errors import DoesNotExist

from database.models import Collections, Products
from libs.errors import InternalServerError
from libs.strings import gettext


class AddProduct(Resource):

    @classmethod
    def post(cls):
        # Get the product payload json
        data = request.get_json()

        # mongodb implementation
        try:
            if "collection" in data:
                collections = []
                # Check if collection exists
                for each in data.get("collection"):
                    try: 
                        collection = Collections.objects.get(title=each)
                    except DoesNotExist:
                        continue

                    if collection:
                        collections.append(collection)
                
                del(data['collection'])

                product = Products(**data)
                if len(collections) > 0:
                    product.collections = collections
                product.save()

                _id = product.id
                return {'id': str(_id)}, 200

            del(data['collection'])
            product = Products(**data)
            product.save()

            _id = product.id
            return {'id': str(_id)}, 200

        except Exception:
             raise Exception


class AllProducts(Resource):

    @classmethod
    def get(cls):
        try:
            products = Products.objects().to_json()
            return Response(products, mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError