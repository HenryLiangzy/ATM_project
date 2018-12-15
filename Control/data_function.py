from os import path

FILENAME = 'account.txt'

def get_path():
    current_path = path.dirname('.')


def test():
    file = open(FILENAME, 'r')
    print(file)


if __name__ == '__main__':
    test()