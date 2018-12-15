from os import path

FILENAME = 'account.txt'


def get_list():
    data_list = []
    file = open(FILENAME, 'r')
    for line in file:
        data = line.split()
        data_list.append(data)
    
    file.close()
    return data_list


def write_list(data_list):
    file = open(FILENAME, 'w')
    for data in data_list:
        string = ' '.join(data)
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