from flask import request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist

from database.models import Products
from libs.strings import gettext


class Product(Resource):

    @classmethod
    def get(cls, id):
        try:
            product = Products.objects.get(id=id)
        except DoesNotExist:
            return {
                    'message': gettext('product_not_exist'),
                    'code': 404
            }, 404

        return Response(product.to_json(), mimetype="application/json", status=200)


    @classmethod
    def put(cls, id):
        data = request.get_json()
        try:
            product = Products.objects.get(id=id)
            product.update(**data)
        except DoesNotExist:
            return {
                'message': gettext('product_not_exist'),
                'code': 404
            }, 404
        
        return {}, 200


    @classmethod
    def delete(cls, id):
        try:
            product = Products.objects.get(id=id)
            product.delete()
        except DoesNotExist:
            return {
                'message': gettext('product_not_exist'),
                'code': 404
            }, 404
        return {}, 200