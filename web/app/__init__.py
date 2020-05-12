from flask_restplus import Api
from flask import Blueprint

# Main

# APIS
from .customers.controller.customer_controller import api as customer_ns

blueprint_api = Blueprint('api', __name__)

api = Api(blueprint_api,
          title='FLASK RESTPLUS API WITH MONGO AND POSTGRES',
          version='1.0',
          description='Api services that shows customer details from mongo and order details from postgres'
          )

api.add_namespace(customer_ns, path='/customer')
