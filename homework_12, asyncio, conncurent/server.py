import socket, asyncio


async def recive_message(sock):
    loop = asyncio.get_event_loop()

    data = await loop.sock_recv(sock, 1024)
    while chr(data[-1]) != "\n":
        data += await loop.sock_recv(sock, 1024)
    return data[:-1]

def calculate(operation, first_number, second_number):
    if operation == "+":
        result = first_number + second_number
        return result
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
    elif operation == "**":
        return first_number ** second_number
    else:
        raise ValueError("invalid operation")
    
    
async def handle_client(socket_client):
    try:
        data = await recive_message(socket_client)
        operation_request = data.decode('utf-8').split()
        loop = asyncio.get_event_loop()
        operation = operation_request[0]
        first_number = float(operation_request[1])
        second_number = float(operation_request[2])
        result = calculate(operation, first_number, second_number)
        await loop.sock_sendall(socket_client, f"{result}\n".encode("utf-8"))
    finally:
        socket_client.close()
        
        
async def s_server(ip, port):
    my_socket = socket.socket()
    my_socket.bind((ip, port))
    my_socket.listen()
    print("listining...")
    my_socket.setblocking(False) # Make socket non blocking to making work with asyncio
    
    loop = asyncio.get_event_loop()
    
    while True:
        socket_client, address_client = await loop.sock_accept(my_socket)
        loop.create_task(handle_client(socket_client))
        
asyncio.run(s_server('127.0.0.1', 8000))
    

    