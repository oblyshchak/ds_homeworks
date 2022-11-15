import socket


def s_client(ip, port, operation,  number_1, number_2):
    my_socket = socket.socket()
    my_socket.connect((ip, port))
    my_socket.send(f"{operation} {number_1} {number_2}\n".encode("utf-8"))
    message = my_socket.recv(1024)
    print(message.decode('utf-8'))    
    
s_client("127.0.0.1", 8000, "**", 180, 90)