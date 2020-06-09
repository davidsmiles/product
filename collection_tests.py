import unittest

from flask_testing import TestCase
from mongoengine.errors import DoesNotExist, InvalidQueryError

from app import app, api
from extensions import *

from database.models import Collections
from libs.errors import *
from resources.routes import initialize_routes


app.config.from_object('config.TestConfig')

# Initialize
initialize_extensions(app)
initialize_routes(api)


class BaseTestCase(TestCase):
    
    def create_app(self):
        return app

    def setUp(self):
        data = {"title": "sports"}

        collection = Collections(**data)
        collection.title = collection.title.lower()
        collection.save()

    def tearDown(self):
        Collections.drop_collection()


class ProductTestCase(BaseTestCase):

    def test_add_collection(self):
        response = self.client.post('/collections/new', 
                                json={
                                    "title": "accessories"
                                }
                        )
        self.assertStatus(response, 200)

    def test_get_all_collections(self):
        response = self.client.get('/collections')
        self.assertStatus(response, 200)

    def test_get_all_products_in_collection(self):
        response = self.client.get('/collections/sports')
        self.assertStatus(response, 200)


if __name__ == '__main__':
    unittest.main()
