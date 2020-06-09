from resources.collections import AddCollection, AllCollections, CollectionProducts
from resources.product import Product
from resources.products import Products


def initialize_routes(api):
    api.add_resource(CollectionProducts, '/collections/<string:title>')
    api.add_resource(AddCollection, '/collections/new')
    api.add_resource(AllCollections, '/collections')
    api.add_resource(Product, '/products/<string:id>')
    api.add_resource(Products, '/products')
