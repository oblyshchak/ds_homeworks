import hashlib
import zlib

capacity = 100
data_base = [None] * capacity


def hash_function(element):
    hash_1 = zlib.crc32(element.encode())
    hash_2 = hashlib.sha256(element.encode()).hexdigest()
    hash_3 = hashlib.sha224(hash_2.encode()).hexdigest()
    return hash_3

def items(data):
    array = []
    for i in data:
        if i is not None:
            array.append(i)
    return array


def index_in_table(key):
    h = zlib.crc32(key.encode())
    return h % capacity

def double_hashing(value, sample_size):
    if sample_size > 1:
        hash_key = index_in_table(value)
        i = 0
        new_index = hash_key
        while data_base[new_index] is not None:
            #new_index = (hash1 + i * hash2) % size
            new_index = (hash_key + hash_key * i) % sample_size
            i += 1
        return new_index 
           

def greeting():
    while True:
        check_user = input('Hi! You are registered user?  Input yes/no:__')
        if check_user == 'yes':
            authorization()
        else:
            registration()

          
def registration():
    print('Hello :)')
    login = input('Input your login for registration, please:__')
    password = input('Input you password for registrtion, please:__')
    repeat_password = input('Input your passworg again, please:__')
    if password != repeat_password:
        print('Incorrect password, try again, text, please SAME passwords')
        return registration
    else:
        index_in_db = index_in_table(login)
        if data_base[index_in_db] is None:
            data_base[index_in_db] = (login, hash_function(password))
        else:
            if data_base[index_in_db][0] == login:
                print('This login in system already, please, use another login for registration')
                return registration
            index = double_hashing(login, capacity)
            data_base[index] = (login, hash_function(password))
    
        print('Congratulations, you have registered :)')
        print('log in to the system, please')
        authorization()

            
def authorization():
    login = input('Input your login for authorization, please:__')
    password = input('Input your password for authorization, please:__')
    if check_data(login, password):
        print(f"Hello, {login}, access granted:)")
        print('You can watch database :)')
        print(items(data_base))
    else:
        attempt = input('Login and password are inccorect. Do you want to try again? (yes/no):__ ')
        if attempt == 'no':
            print("goodbye :)")
        else:
            return authorization()

        
def check_data(login, password):
    index = index_in_table(login)
    key, value = data_base[index]
    if key == login:
        if value == hash_function(password):
            return True
        return False
    else:
        new_index = double_hashing(login, capacity)
        key_2, value_2 = data_base[new_index]
        if key_2 == login:
            if value_2 == hash_function(password):
                return True
            return False
        
print(greeting())
    
    
        



