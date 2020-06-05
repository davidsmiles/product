from flask_restful import HTTPException


class ResourceExists(HTTPException):
    pass


class ResourceNotExist(HTTPException):
    pass


class QueryInvalidError(HTTPException):
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
    "ResourceExists": {
        "message": "The request resource already exists",
        "status": 404
    },
    "ResourceNotExist": {
        "message": "The requested resource does not exist",
        "status": 404
    },
    "QueryInvalidError": {
        "message": "Sorry, could not resolve field(s) sent in with request",
        "status": 500
    },
    "InternalServerError": {
        "message": "Oops, something went wrong",
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