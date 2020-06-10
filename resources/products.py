import requests

from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, InvalidQueryError

from libs.errors import InternalServerError, QueryInvalidError
from libs.strings import gettext


class Products(Resource):

    @classmethod
    @jwt_optional
    def post(cls):
        
        from database.models import Collections, Products

        # Get the product payload json
        data = request.get_json()

        # mongodb implementation
        try:
            if "collections" in data:
                collections = []
                # Check if collection exists
                for each in data.get("collections"):
                    try: 
                        collection = Collections.objects.get(title=each.lower())
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
             raise Exception

    @classmethod
    def get(cls):
        from database.models import Collections, Products
        try:
            query = request.values  # ?tags=sportswear&type=shirt
            products = Products.objects(**query).to_json()
            return Response(products, mimetype="application/json", status=200)
        except InvalidQueryError:
            raise QueryInvalidError
        except Exception:
            raise InternalServerError
