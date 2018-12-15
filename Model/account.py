class account(object):
    
    def __init__(self, number, name, passwd, balance, vip, update_time):
        self.__number = number
        self.__name = name
        self.__passwd = passwd
        self.__balance = balance
        self.__vip = vip
        self.__update_time = update_time

    def get_number(self):
        return self.__number

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

    def set_number(self, number):
        self.__number = number

    def set_name(self, name):
        self.__name = name
    
    def set_passwd(self, passwd):
        self.__passwd = passwd

    def set_balance(self, balance):
        self.__balance
    
    def set_vip(self, vip):
        self.__vip = vip

    def set_update_time(self, update_time):
        self.__update_time = update_time

    def get_customer(self):
        new_string = str(
            self.__number + ' ' + self.__name + ' ' + self.__passwd + ' '
            + self.__balance + ' ' + self.__vip + ' ' + self.__update_time
        )

        return new_string