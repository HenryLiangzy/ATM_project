
# coding: utf-8

# In[ ]:


import datetime


FILEPATH = 'account.txt'


# the below is class object and including function
class account(object):
    
    def __init__(self, id, name, passwd, balance, vip, update_time):
        self.__id = id
        self.__name = name
        self.__passwd = passwd
        self.__balance = balance
        self.__vip = vip
        self.__update_time = update_time
        
    # basic method for class operation
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_passwd(self):
        return self.__passwd
    
    def get_balance(self):
        return self.__balance
    
    def get_vip(self):
        return self.__vip
    
    def get_update_time(self):
        return self.__update_time
    
    def set_passwd(self, passwd):
        self.__passwd = str(passwd)
        
    def set_balance(self, balance):
        self.__balance = str(balance)
        
    def set_update_time(self):
        current = datetime.datetime.now()
        time_string = current.strftime('%Y-%m-%d')
        self.__update_time = str(time_string)
        
    def get_account(self):
        string = str(
            self.get_id() + ' ' + self.get_name() + ' ' + self.get_passwd() + ' ' + self.get_balance() + ' ' + self.get_vip() +
            ' ' + self.get_update_time() + '\n'
        )
        
        return string
    
    def update_balance(self):
        last_time = datetime.datetime.strptime(self.get_update_time(), "%Y-%m-%d")
        current_time = datetime.datetime.now()
        difference =  current_time - last_time
        if difference.days > 0:
            balance = float(self.get_balance())
            if self.get_vip == 'V':
                rate = 0.000012
            else:
                rate = 0.00001
            
            for times in range(difference.days):
                balance = balance * (rate + 1)
                # balance *= rate+1
            
            self.set_balance(str(balance))
            self.set_update_time()
    
    
    # the class method down below is for atm function
    def inquiry(self):
        self.update_balance()
        return self.get_name(), self.get_balance()
        
        
    def deposit(self, deposit_num):
        self.update_balance()
        balance = float(self.get_balance()) + float(deposit_num)
        self.set_balance(str(balance))
        
        return balance
        
        
    def withdraw(self, withdraw_num):
        self.update_balance()
        balance = float(self.get_balance())
        withdraw_num = float(withdraw_num)
        if withdraw_num > 2000 and self.get_vip() == 'N':
            print("WARNING: Out of withdraw limit")
            return False
        elif withdraw_num > 3000 and self.get_vip() == 'V':
            print("WARNING: Out of withdraw limit")
            return False
        elif withdraw_num > balance:
            print("ERROR: You are out of your balance, your balance is", self.get_balance())
            return False
        else:
            self.set_balance(str(balance - withdraw_num))
            return True


    def transfer(self, target, transfer_num):
        self.update_balance()
        balance = float(self.get_balance())
        transfer_num = float(transfer_num)
        if transfer_num > 10000 and self.get_vip() == 'N':
            print("WARNING: Out of transfer limit")
            return False
        elif transfer_num > 20000 and self.get_vip() == 'V':
            print("WARNING: Out of transfer limit")
            return False
        elif transfer_num > balance:
            print("ERROR: You are out of your balance, your balance is", self.get_balance())
            return False
        else:
            self.set_balance(str(balance - transfer_num))
            target.set_balance(str(float(target.get_balance()) + transfer_num))
            return True
        
        
# down below is system function
def read_list():
    with open(FILEPATH, 'r') as file:
        data = file.readlines()
    
    customer_list = []
    for line in data:
        e = line.split()
        customer = account(e[0], e[1], e[2], e[3], e[4], e[5])
        customer_list.append(customer)
        
    return customer_list


def write_list(customer_list):
    try:
        with open(FILEPATH, 'w') as file:
            for customer in customer_list:
                file.write(customer.get_account())
        print('File save successful')
    except IOError as e:
        print(e)
    finally:
        return None
        

def login(customer_list, input_number, input_passwd):
    for customer in customer_list:
        if input_number == customer.get_id():
            if input_passwd == customer.get_passwd():
                return True, customer_list.index(customer)
            else:
                return False, 'ERROR: Password not correct'
    else:
        return False, 'ERROR: Customer not found'


def atm_inqury(customer_list, index):
    customer_name, balance = customer_list[index].inquiry()
    print('\n\nDear', customer_name, ', your balance is', balance)
    
    return customer_list


def atm_deposit(customer_list, index):
    amount = input("\n\tPlease input the amount to save:")
    balance = customer_list[index].deposit(amount)
    print("\n\tDear", customer_list[index].get_name(), ", your balance has been update to", balance)
    
    return customer_list


def atm_withdraw(customer_list, index):
    amount = input("\n\tPlease input the amount to withdraw:")
    if customer_list[index].withdraw(amount):
        print("\n\tDear", customer_list[index].get_name(), ", your balance has been update to", customer_list[index].get_balance())
    
    return customer_list


def atm_transfer(customer_list, index):
    target_id = input("\n\tPlease input the taget account numer:")
    for target in customer_list:
        if target.get_id() == target_id:
            amount = input("\tPlease input the amount to transfer:")
            if customer_list[index].transfer(target, amount):
                print("Transfer successful! Your balance have been update to", customer_list[index].get_balance())
                break
    else:
        print("\nERROR: Target account is invaild")
    
    return customer_list


def display():
    customer_list = read_list()
    
    # login part
    while(True):
        input_name = input("Please input your account number:")
        input_passwd = input("Please input your password:")
        
        result, detail = login(customer_list, input_name, input_passwd)
        if result is False:
            print(detail)
            continue
        elif result is True:
            break
    
    # main menu
    while(True):
        print("\n\n")
        print("\t1. Inquiry")
        print("\t2. Deposit")
        print("\t3. Withdraw")
        print("\t4. Transfer")
        print("\t5. Quit")
        
        print("\n\n")
        
        choose = int(input("\n\nPlease select:"))
        
        if choose == 1:
            customer_list = atm_inqury(customer_list, detail)
        elif choose == 2:
            customer_list = atm_deposit(customer_list, detail)
        elif choose == 3:
            customer_list = atm_withdraw(customer_list, detail)
        elif choose == 4:
            customer_list = atm_transfer(customer_list, detail)
        elif choose == 5:
            # write_list(customer_list)
            break
        else:
            print("Please input 1~5 to select")
            continue
        
        # end of each step, ask if continue or not
        print("\n")
        print("\t1. Continue")
        print("\t2. Quit")
        select = input("Select 1 or 2\n>>")
        if select == '2':
            # write_list(customer_list)
            break


def test():
    customer_list = read_list()
    print(login(customer_list, '0123', '123456'))
    customer = account('0123', 'Ryan', '123456', '10000.23', 'V', '2018-01-01_03:58:30')
    customer.deposit(300)
    customer.withdraw(0.23)
    print(customer.inquiry())
    print(customer.get_account())

if __name__ == '__main__':
    display()
    # test()

