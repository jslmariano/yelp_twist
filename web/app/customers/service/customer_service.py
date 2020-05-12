
from app.customers.model.customer import Customer
from app.main import mongo

def get_all_customers():

    customer_list = []
    for customer in Customer.objects:
        customer_dict = dict()
        customer_dict['user_id'] = customer.user_id
        customer_dict['login'] = customer.login
        customer_dict['name'] = customer.name
        customer_dict['company_id'] = customer.company_id
        customer_dict['password'] = customer.password
        customer_dict['credit_cards'] = customer.credit_cards
        customer_list.append(customer_dict)

    return customer_list

def save_customer(user_id, login, password,
                  name, company_id, credit_cards):

    customer_model = Customer(user_id=user_id, login=login,
                            password=password, name=name,
                            company_id=company_id, credit_cards=credit_cards,)
    result = customer_model.save()

    return result