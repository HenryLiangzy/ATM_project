from Control import data_function
import Model.account

def login(customer_list, input_name, input_passswd):
    for customer in customer_list:
        if customer.get_name() == input_name:
            if input_passswd == customer.get_passwd():
                return True, customer
    
    return False


def inquiry(customer):
    return customer.get_balance


def deposit(customer, deposit_num):
    current_balance = float(customer.get_balance())
    customer.set_balance(str(current_balance + float(deposit_num)))


def withdraw(customer, withdraw_num):
    balance = float(customer.get_balance())
    if customer.get_vip == 'V' and withdraw_num > 3000:
        print("WARNING: Out of the withdraw limit")
        return False
    elif customer.get_vip == 'N' and withdraw_num > 2000:
        print("WARNING: Out of the withdraw limit")
        return False
    elif withdraw_num > balance:
        print("ERROR: Out of the account balance")
        return False
    else:
        customer.set_balance(str(balance - withdraw_num))
        return True


def transfer(customer, target_customer, transfer_num):
    balance = float(customer.get_balance())
    if customer.get_vip == 'V' and transfer_num > 20000:
        print("WARNING: Out of the transfer limit")
        return False
    elif customer.get_vip == 'N' and transfer_num > 10000:
        print("WARNING: Out of the transfer limit")
        return False
    elif transfer_num > balance:
        print("ERROR: Out of the account balance")
        return False
    else:
        customer.set_balance(str(balance - transfer_num))
        target_customer.set_balance(str(float(target_customer.get_balance()) + transfer_num))
        return True


if __name__ == '__main__':
    customer_list = data_function.get_list()
    print(login(customer_list, 'Ryan', '123456'))