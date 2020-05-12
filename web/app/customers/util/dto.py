from flask_restplus import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'user_id': fields.String(description='customer Identifier'),
        'login': fields.String(required=True, description='customer login'),
        'name': fields.String(required=True, description='customer name'),
        'company_id': fields.String(required=True, description='customer company identifier'),
        'password': fields.String(required=True, description='customer password'),
        'credit_cards': fields.String(required=True, description='customer credit cards'),
    })

class CompanyDto:
    api = Namespace('company', description='company related operations')
    company = api.model('company', {
        'company_id': fields.String(description='company Identifier'),
        'company_name': fields.String(required=True, description='company name'),
    })
