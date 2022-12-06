class ConnectionError(Exception):
    def __init__(self, host, user, password, message):
        self.host = host
        self.user = user
        self.password = password
        self.message = message

    def __str__(self):
        return f"Connection to server MySQL with name {self.user}, host {self.host} is not established: {self.message}"

class SyntaxMySQLError(Exception):
    def __init__(self, message, data):
        self.message = message
        self.data = data

    def __str__(self):
        return f"You have some problems with ____{self.data}____ syntax:  {self.message}"

class KeyError(Exception):
    def __init__(self, message, data):
        self.message = message


    def __str__(self):
        return f"KEY ERROR ___{self.data}____:  {self.message}"