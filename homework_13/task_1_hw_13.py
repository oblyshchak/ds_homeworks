from random_words import RandomWords
import random
import time

def create_int_list(number):
    int_list = []
    for i in range(number):
        int_list.append(random.randint(0, 1000))
    return int_list


def create_float_list(number):
    float_list = []
    for i in range(number):
        float_list.append(random.uniform(0.1, 100.0))
    return float_list


def create_str_list(number):
    w = RandomWords()
    list_words = []
    for i in range(number):
        list_words.append(w.random_word())
    return list_words

# if __name__ == "__main__":
#     start_int = time.time()
#     create_int_list(5000)
#     finish_int = time.time()
#     print("INT")
#     print(finish_int-start_int)
#     start_float = time.time()
#     create_float_list(5000)
#     finish_float = time.time()
#     print("FLOAT")
#     print(finish_float-start_float)
#     start_str = time.time()
#     create_str_list(5000)
#     finish_str = time.time()
#     print("STR")
#     print(finish_str-start_str)
