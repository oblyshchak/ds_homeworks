import concurrent.futures
import time 

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

def main(arguments):
    start_1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(factorial, argument): argument for argument in arguments
        }
        for future in concurrent.futures.as_completed(futures):
            argument = futures[future]
            print(f"Result of {argument} is {future.result()}")

    end_1 = time.time()

    result_thread_time = end_1 - start_1
    return result_thread_time
    

def main_2(arguments):
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        futures = {
            executor.submit(factorial, argument) : argument for argument in arguments
        }
        for future in concurrent.futures.as_completed(futures):
            argument = futures[future]
            print(f"Result of {argument} is {future.result()}")
            
    finish = time.time()
    
    result_process_time = finish - start
    return result_process_time

list_for_compare = [234, 78, 45, 12]
if __name__ == '__main__':
    thread_time = main(list_for_compare)
    process_time = main_2(list_for_compare)
    if thread_time > process_time:
        print(f"PROCESS TIME: {process_time} is faster")
    else:
        print(f"THREAD TIME: {thread_time} is faster")

