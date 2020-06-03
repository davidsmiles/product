from flask import request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from libs.strings import gettext
from models.product import Products


class Product(Resource):
    @classmethod
    def get(cls, title):
        product = Products.objects.get(title=title).to_json()
        return Response(product, mimetype="application/json", status=200)

    @classmethod
    def put(cls, title):
        data = request.get_json()
        Products.objects.get(title=title).update(**data)
        return '', 200

    @classmethod
    def delete(cls, title):
        Products.objects.get(title=title).delete()
        return '', 200