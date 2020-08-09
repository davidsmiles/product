from app import app, api
from extensions import *
from resources.routes import initialize_routes

initialize_extensions(app)
initialize_routes(api)
