import requests
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, InvalidQueryError

from database.models import Collections, Products
from libs.errors import InternalServerError, QueryInvalidError
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

                product = Products(**data)
                if len(collections) > 0:
                    product.collections = collections
                product.save()

                _id = product.id
                return {'id': str(_id)}, 200

            product = Products(**data)
            product.collections = []
            product.save()

            _id = product.id
            return {'id': str(_id)}, 200

        except Exception:
             raise InternalServerError


class AllProducts(Resource):

    @classmethod
    def get(cls):
        try:
            query = request.values
            products = Products.objects(**query).to_json()
            return Response(products, mimetype="application/json", status=200)
        except InvalidQueryError:
            raise QueryInvalidError
        except Exception:
            raise InternalServerError