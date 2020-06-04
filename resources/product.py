from flask import request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from database.models import Products
from libs.strings import gettext


class Product(Resource):
    @classmethod
    def get(cls, title):
        product = Products.objects.get(title=title)
        if not product:
            return {
                'message': gettext('product_not_exist'),
                'code': 404
            }, 404

        return Response(product.to_json(), mimetype="application/json", status=200)

    @classmethod
    def put(cls, title):
        data = request.get_json()
        product = Products.objects.get(title=title)
        if not product:
            return {
                'message': gettext('product_not_exist'),
                'code': 404
            }, 404
        
        product.update(**data)
        return '', 200

    @classmethod
    def delete(cls, title):
        products.objects.get(title=title)
        if not product:
            return {
                'message': gettext('product_not_exist'),
                'code': 404
            }, 404

        product.delete()
        return '', 200