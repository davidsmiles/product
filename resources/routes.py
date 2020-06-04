from resources.collections import AddCollection, AllCollections, Collection
from resources.product import Product
from resources.products import AddProduct, AllProducts


def initialize_routes(api):
    api.add_resource(Collection, '/collections/<string:title>')
    api.add_resource(AddCollection, '/collections/new')
    api.add_resource(AllCollections, '/collections')
    api.add_resource(Product, '/products/<string:_id>')
    api.add_resource(AddProduct, '/products/new')
    api.add_resource(AllProducts, '/products')
