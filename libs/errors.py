from flask_restful import HTTPException


class CollectionExistsError(HTTPException):
    pass

class InternalServerError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


class ProductsNotExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


errors = {
    "CollectionExistsError": {
        "message": "Collection already exists",
        "status": 204
    },
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "ProductsNotExistsError": {
        "message": "Products with given name doesnt' exists",
        "status": 400
    }
}