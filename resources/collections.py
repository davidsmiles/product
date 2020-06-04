import requests
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from database.models import Collections
from libs.strings import gettext


class AddCollection(Resource):

    @classmethod
    def post(cls):
        # Get the product payload json
        data = request.get_json()

        # mongodb implementation
        collection = Collections.objects.get(name=data.get('name'))
        
        if collection:
            return {
                "message": "collection already exists",
                "status": 204
            }
            
        collection = Collections(**data)
        collection.save()
        
        return {}, 200


class AllCollections(Resource):

    @classmethod
    def get(cls):
        collections = Collections.objects().to_json()
        return Response(collections, mimetype="application/json", status=200)