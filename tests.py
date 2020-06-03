import unittest

from flask_testing import TestCase

from app import app
from extensions import db
from models.item import ItemModel


class BaseTestCase(TestCase):
    
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(
            ItemModel(
                name='samsung a30s',
                description='a really incredible mobile phone',
                price=12.00
            )
        )
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class ProductTestCase(BaseTestCase):

    def test_add_product(self):
        response = self.client.post('/products/items', 
                        json=[{
                                "name": "eyelash",
                                "description": "a very nice eyelash",
                                "price": 20.00
                            },
                            {
                                "name": "hello",
                                "description": "really nice",
                                "price": 33
                            }
                            ])
        self.assertStatus(response, 200)

    def test_get_all_products(self):
        response = self.client.get('/products/items')
        self.assertStatus(response, 200)

    def test_get_product(self):
        response = self.client.get('/products/items/1')
        self.assertStatus(response, 200)

    def test_update_product(self):
        response = self.client.put('/products/items/1', 
                        json={
                                "name": "facelash",
                                "description": "a very nice eyelash",
                                "price": 27.00
                            })
        self.assertStatus(response, 200)

    def test_delete_product(self):
        response = self.client.delete('/products/items/1')
        self.assertStatus(response, 204)


if __name__ == '__main__':
    unittest.main()
