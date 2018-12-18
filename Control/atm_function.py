import data_function
import Model.account

def login(customer_list, input_name, input_passswd):
    for customer in customer_list:
        if customer.get_name() == input_name:
            if input_passswd == customer.get_passwd():
                return True, customer
    
    return False


def inquiry(customer):
    return customer.get_balance


if __name__ == '__main__':
    customer_list = data_function.get_list()
    print(login(customer_list, 'Ryan', '123456'))