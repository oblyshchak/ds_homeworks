from task_1_hw_13 import create_float_list, create_int_list, create_str_list
import time

def bubble_sort(array_list):
    n = len(array_list)
    for i in range(n):
        swap = True
        for element_index in range(n - i - 1):
            if array_list[element_index] > array_list[element_index + 1]:
                array_list[element_index], array_list[element_index + 1] = array_list[element_index + 1], array_list[element_index]
                swap = False
        if swap:
            break
    return array_list

def average_time(function, array_list, n):
    av_time = 0
    for i in range(n):
        start_time = time.time()
        function(array_list[:])
        finish_time = time.time()
        av_time += finish_time - start_time

    result = av_time/n
    print(f"{function.__name__} executed {n} times, average values = {result} second")
    return result

print(average_time(bubble_sort, create_str_list(5000), 10))