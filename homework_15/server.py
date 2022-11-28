import logging
import socket

logging.basicConfig(level=logging.DEBUG, filename='log_server.log', format='server %(asctime)s - %(levelname)s - %(message)s')

try:
    my_socket = socket.socket()
    my_socket.bind(("127.0.0.1", 8000))
    my_socket.listen()
    logging.info("listening")
except Exception as err:
    logging.error(f"failed to start server")
else:
    while True:
        client_socket, client_address = my_socket.accept()
        logging.debug(f"server accept {client_address}")
        while True:
            try:
                info_from_client = client_socket.recv(1024)
            except Exception as error:
                logging.error(f"server couldn't receive 1024 b from {client_socket}")
                client_socket.close()
                break
            message_to_client = input("Send message to client, if you want break, input q:__")
            if message_to_client == "q":
                break
            logging.debug(f"Sending message to client")
            client_socket.send(message_to_client.encode())

        client_socket.close()
finally:
    logging.info(f"socket {my_socket} closing")
    my_socket.close()



