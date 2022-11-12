import socket

def recive_message(sock):
    data = sock.recv(1024)
    while chr(data[-1]) != "\n":
        data += sock.recv(1024)
    return data[:-1]

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8000))
message_from_server = recive_message(my_socket)

print(message_from_server)
message_to_server = input("Enter number of month:__")
my_socket.send(message_to_server.encode())

message_from_server = recive_message(my_socket)
print(message_from_server)
my_socket.close()
