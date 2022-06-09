#  You can experiment here, it won’t be checked
import itertools
import string


def find_password(repeat):
    const = string.ascii_letters + string.digits
    for rep in range(1, repeat + 1):
        for i in itertools.product(const, repeat=rep):
            yield ''.join(i)


def connect():
    for i in find_password(10):
        if i == "Conn":
            print(i)
            break


if __name__ == '__main__':
    connect()
