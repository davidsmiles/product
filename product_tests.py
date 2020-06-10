import unittest

from flask_testing import TestCase
from mongoengine.errors import DoesNotExist, InvalidQueryError

from app import app, api
from extensions import *

from database.models import Products, Collections
from libs.errors import *
from resources.routes import initialize_routes


app.config.from_object('config.TestConfig')


# Initialize
initialize_extensions(app)
initialize_routes(api)


product_id = 0


class BaseTestCase(TestCase):
    
    def create_app(self):
        return app

    def setUp(self):
        global product_id

        data = {
            "title": "Madrid Jersey",
            "description": "Very beautiful round neck shirt",
            "pricing": {
                "price": 120,
                "compare_at_price": 130,
                "cost_per_item": 110
            },
            "inventory": {
                "sku": "unique_store_keeping_unit_value",
                "quantity": 10,
                "track_quantity": True
            },
            "type": "shirt",
            "vendor": "D&G",
            "tags": ["attire", "native"],
            "variants": {
                "size": ["10", "11", "12"],
                "color": ["red", "blue"]
            },
            "collections": ["sports"]}
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

            product_id = str(_id)

            return {'id': str(_id)}, 200

        product = Products(**data)
        product.collections = []
        product.save()

        product_id = product.id

    def tearDown(self):
        Products.drop_collection()


class ProductTestCase(BaseTestCase):

    def test_add_product(self):
        response = self.client.post('/products', 
                                json={
                                    "title": "Madrid Jersey",
                                    "description": "Very beautiful round neck shirt",
                                    "pricing": {
                                        "price": 120,
                                        "compare_at_price": 130,
                                        "cost_per_item": 110
                                    },
                                    "inventory": {
                                        "sku": "unique_store_keeping_unit_value",
                                        "quantity": 10,
                                        "track_quantity": True
                                    },
                                    "type": "shirt",
                                    "vendor": "D&G",
                                    "tags": ["attire", "native"],
                                    "variants": {
                                        "size": ["10", "11", "12"],
                                        "color": ["red", "blue"]
                                    },
                                    "collections": ["sports"]
                                }
                        )
        self.assertStatus(response, 200)

    def test_get_all_products(self):
        response = self.client.get('/products')
        self.assertStatus(response, 200)

    def test_get_product(self):
        response = self.client.get(f'/products/{product_id}')
        self.assertStatus(response, 200)

    def test_update_product(self):
        response = self.client.put(f'/products/{product_id}', 
                        json={
                                "title": "test-product"
                            })
        self.assertStatus(response, 200)

    def test_delete_product(self):
        response = self.client.delete(f'/products/{product_id}')
        self.assertStatus(response, 200)


if __name__ == '__main__':
    unittest.main()
