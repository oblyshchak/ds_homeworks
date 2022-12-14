import socket

my_socket = socket.socket()
my_socket.bind(("127.0.0.1", 8000))
my_socket.listen()
print("server listening")

while True:
    client_socket, client_address = my_socket.accept()
    while True:
        info_from_client = client_socket.recv(1024)
        print(info_from_client)
        mesagge_to_client = input("Send message to client, if you want break, input q:__")
        if mesagge_to_client == "q":
            break
        client_socket.send(mesagge_to_client.encode())
            
    client_socket.close()
    
my_socket.close()