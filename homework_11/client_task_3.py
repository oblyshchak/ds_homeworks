import socket


def s_client(message, ip, port):
    my_socket = socket.socket()
    my_socket.connect((ip, port))
    format_message = message.encode()
    my_socket.send(format_message)
    message_from_server = my_socket.recv(1024)
    print(message_from_server)
    my_socket.close()
    return message_from_server

message = "Hello, I'm client!"
message_test = "REST API design is a huge topic with many layers. As with most things in technology, there’s a wide range of opinions on the best approach to building APIs. In this section, you’ll look at some recommended steps to follow as you build an API."
s_client(message_test, "127.0.0.1", 8000)