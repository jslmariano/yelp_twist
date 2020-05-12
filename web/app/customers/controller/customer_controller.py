from flask import request
from flask_restplus import Resource

from ..util.dto import CustomerDto
from ..service.customer_service import get_all_customers

api = CustomerDto.api
_customer = CustomerDto.customer

@api.route('/')
class CustomerList(Resource):

    @api.doc('list_of_registered_customer')
    def get(self):
        """List all registered users"""
        return get_all_customers()

