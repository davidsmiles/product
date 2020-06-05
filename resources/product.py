from flask import request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist

from database.models import Products
from libs.errors import ResourceNotExist
from libs.strings import gettext


class Product(Resource):

    @classmethod
    def get(cls, id):
        try:
            product = Products.objects.get(id=id)
            return Response(product.to_json(), mimetype="application/json", status=200)
        except DoesNotExist:
            raise ResourceNotExist


    @classmethod
    def put(cls, id):
        data = request.get_json()
        try:
            product = Products.objects.get(id=id)
            product.update(**data)
        except DoesNotExist:
            raise ResourceNotExist
        
        return {}, 200


    @classmethod
    def delete(cls, id):
        try:
            product = Products.objects.get(id=id)
            product.delete()
        except DoesNotExist:
            raise ResourceNotExist
        
        return {}, 200