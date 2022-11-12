import socket

def s_server(ip, port):
    my_socket = socket.socket()
    my_socket.bind(("127.0.0.1", 8000))
    my_socket.listen()
    print("listening")
    
    client_socket, client_address = my_socket.accept()
    message_from_client = client_socket.recv(1024)
    format_msg_client = message_from_client.decode('utf-8')
    result_list = format_msg_client.split()
    ready_to_send = str(len(result_list))
    client_socket.send(ready_to_send.encode())
    client_socket.close()
    my_socket.close()

s_server("127.0.0.1", 8000)

