import requests
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError

from database.models import Collections, Products
from libs.errors import ResourceExists, ResourceNotExist
from libs.strings import gettext


class CollectionProducts(Resource):
    
    @classmethod
    def get(cls, title: str):
        try:
            collection = Collections.objects.get(title=title.lower())

            if collection:
                products = Products.objects(collections__in=[collection])
            
                return Response(products.to_json(), mimetype="application/json", status=200)
        except DoesNotExist:
           raise ResourceNotExist


class AddCollection(Resource):

    @classmethod
    def post(cls):
        # Get the product payload json
        data = request.get_json()

        # mongodb implementation
        try:    
            collection = Collections(**data)
            collection.title = collection.title.lower()
            collection.save()
        except NotUniqueError:
            raise ResourceExists

        return {"id": str(collection.id)}, 200


class AllCollections(Resource):

    @classmethod
    def get(cls):
        collections = Collections.objects().to_json()
        return Response(collections, mimetype="application/json", status=200)