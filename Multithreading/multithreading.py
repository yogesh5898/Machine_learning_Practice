import time
import threading

"""I/O operation is performing to read or access a file """

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f'Number : {i}', end='\n')


def print_letter():
    for i in 'abcde':
        time.sleep(2)
        print(f'Letters : {i}', end='\n')


start_time = time.time()
""" Create 2 thread """
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)

"""start the thread"""
t1.start()
t2.start()

""" wait for the threads to get complete """
t1.join()
t2.join()

finish_time = time.time() - start_time
print(finish_time)
