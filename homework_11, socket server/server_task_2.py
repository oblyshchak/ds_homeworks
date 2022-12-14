import socket 

my_socket = socket.socket()
my_socket.bind(("127.0.0.1", 8000))
my_socket.listen()
print("listening")
client_socket, client_address = my_socket.accept()
season = {
        "1" :'January',
        2 : 'February',
        3 : 'March',
        4 : 'April', 
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'September', 
        10 : 'October',
        11 : 'Novemver',
        12 : 'December'
    }
client_socket.send(b"You can ask me number of month and I give you a name this month :)\n")
question_from_client = client_socket.recv(1024)
question_format = int(question_from_client.decode("utf-8"))
print(question_format)
if (question_format) not in season.keys():
    client_socket.send(b"Error: This is number of month invalid, try again")
else:
    ansver = season[question_format]
    client_socket.send(ansver.encode())
    client_socket.send(b'\n')
    client_socket.close()
    
my_socket.close()

