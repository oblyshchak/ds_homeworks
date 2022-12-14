import logging
import socket

logging.basicConfig(level=logging.DEBUG, filename='log_server.log', format='client %(asctime)s - %(levelname)s - %(message)s')

my_socket = socket.socket()
logging.info("client trying to connect to server")
my_socket.connect(("127.0.0.1", 8000))
logging.info('client connected')

while True:
    message_to_server = input("Text message to server, if you want brake input q:__")
    if message_to_server == "q":
        break
    logging.debug(f"sending to server {message_to_server}")
    my_socket.send(message_to_server.encode())
    message_from_server = my_socket.recv(1024)
    if message_from_server:
        logging.debug(f"{my_socket} get from server {message_from_server}")
    else:
        logging.error(f"couldn't get message from server")
        my_socket.close()
my_socket.close()