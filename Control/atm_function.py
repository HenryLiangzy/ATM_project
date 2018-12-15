import data_function

def login(data_list, input_name, input_passswd):
    if input_name not in data_list:
        return False
    
    