class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class ProductsNotExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


errors = {
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