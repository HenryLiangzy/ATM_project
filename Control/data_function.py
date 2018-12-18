from os import path
import sys
sys.path.append('.')
from Model.account import account

FILENAME = 'account.txt'


def get_list():
    customer_list = []
    file = open(FILENAME, 'r')
    for line in file.readlines():
        data = line.split()
        customer = account(data[0], data[1], data[2], data[3], data[4], data[5])
        customer_list.append(customer)
    
    file.close()
    return customer_list


def write_list(customer_list):
    with open(FILENAME, 'w') as file:
        for customer in customer_list:
            file.writelines(customer.get_customer())
    
    return None


def test():
    file = open(FILENAME, 'r')
    print(file.readlines())


if __name__ == '__main__':
    list = get_list()
    # for element in list:
    #     print(element.get_customer())
    # test()