class account(object):
    
    def __init__(self, number, name, passwd, balance, vip, update_time):
        self.__number = number
        self.__name = name
        self.__passwd = passwd
        self.__balance = balance
        self.__vip = vip
        self.__update_time = update_time

    def get_number():
        return self.__number

    def get_name():
        return self.__name

    def get_passwd():
        return self.__passwd

    def get_balance():
        return self.__balance

    def get_vip():
        return self.__vip
    
    def get_update_time():
        return self.__update_time

    def set_number(number):
        self.__number = number

    def set_name(name):
        self.__name = name
    
    def set_passwd(passwd):
        self.__passwd = passwd

    def set_balance(balance):
        self.__balance
    
    def set_vip(vip):
        self.__vip = vip

    def set_update_time(update_time):
        self.__update_time = update_time
    