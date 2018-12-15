from os import path
import Model.account

FILENAME = 'account.txt'


def get_list():
    customer_list = []
    file = open(FILENAME, 'r')
    for line in file:
        data = line.split()
        customer = account(data[0], data[1], data[2], data[3], data[4], data[5])
        customer_list.append(customer)
    
    file.close()
    return customer_list


def write_list(customer_list):
    file = open(FILENAME, 'w')
    for customer in customer_list:
        string = customer.get_list()
        file.writelines(string)
    
    file.close()
    return None


def test():
    file = open(FILENAME, 'r')
    print(file.read())


if __name__ == '__main__':
    list = get_list()
    # for data in list:
    #     string = ' '.join(data)
    #     print(string)
    write_list(list)
    print(get_list())