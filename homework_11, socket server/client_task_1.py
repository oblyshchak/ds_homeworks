import socket

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8000))

while True:
    message_to_server = input("Text message to server, if you want brake input q:__")
    if message_to_server == "q":
        break
    my_socket.send(message_to_server.encode())
    message_from_server = my_socket.recv(1024)
    print(message_from_server)
        
my_socket.close()
