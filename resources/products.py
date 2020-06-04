import requests
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from database.models import Collections, Products
from libs.errors import InternalServerError, SchemaValidationError
from libs.strings import gettext


class AddProduct(Resource):

    @classmethod
    def post(cls):
        # Get the product payload json
        data = request.get_json()

        # mongodb implementation
        try:
            if "collection" in data:
                collection = Collections.objects.get(name=data.get("collection"))
                del(data['collection'])

                if collection:
                    product = Products(**data)
                    product.collection = collection
                    product.save()

                    id = product.id
                    return {'id': str(id)}, 200

                product = Products(**data)
                product.save()

                _id = product.id
                return {'id': str(_id)}, 200

        except SchemaValidationError:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError


class AllProducts(Resource):

    @classmethod
    def get(cls):
        try:
            products = Products.objects().to_json()
            return Response(products, mimetype="application/json", status=200)

        except Exception:
            raise InternalServerError