import requests
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from database.models import Products
from libs.strings import gettext


class AddProduct(Resource):

    @classmethod
    def post(cls):
        # Get the product payload json
        data = request.get_json()

        # mongodb implementation
        product = Products(**data)
        product.save()

        id = product.id
        
        return {'id': str(id)}, 200


class AllProducts(Resource):

    @classmethod
    def get(cls):
        products = Products.objects().to_json()
        return Response(products, mimetype="application/json", status=200)
