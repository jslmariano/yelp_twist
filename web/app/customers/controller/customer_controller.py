from flask import request
from flask_restplus import Resource

from ..util.dto import CustomerDto
from ..service.customer_service import *

api = CustomerDto.api
_customer = CustomerDto.customer

@api.route('/')
class CustomerList(Resource):

    @api.doc('list_of_registered_customer')
    def get(self):
        """List all registered users"""
        return get_all_customers()


@api.route('/add')
class CustomerCsv(Resource):

    @api.doc('list_of_customers_in_csv')
    def get(self):
        """List all registered users"""
        customer_dict = dict()
        customer_dict['user_id']='josel'
        customer_dict['login']='josel'
        customer_dict['password']='josel'
        customer_dict['name']='josel'
        customer_dict['company_id']='1'
        customer_dict['credit_cards']= "[***3421]"
        return save_customer(**customer_dict)


@api.route('/csv')
class CustomerCsv(Resource):

    @api.doc('save_customers_from_csv')
    def get(self):
        """List all registered users"""
        return save_customers_from_csv()


@api.route('/test')
class CustomerCsv(Resource):

    @api.doc('just_a_test')
    def get(self):
        """List all registered users"""
        return {'message': 'Hello, I am your backend'}


@api.route('/delete_all')
class CustomerDeleteAll(Resource):

    @api.doc('delete_all_customers_in_mongodb')
    def get(self):
        """List all registered users"""
        return delete_all_customer()

