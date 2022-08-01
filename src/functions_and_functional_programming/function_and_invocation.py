import socket


def resolve(host):
    print(socket.gethostbyname(host))


resolve('google.com')
