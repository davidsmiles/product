from resources.product import Product
from resources.products import AddProduct, AllProducts


def initialize_routes(api):
    api.add_resource(Product, '/products/<string:title>')
    api.add_resource(AddProduct, '/products/new')
    api.add_resource(AllProducts, '/products')
