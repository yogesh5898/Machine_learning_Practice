import time
import multiprocessing


def square_number():
    for i in range(5):
        time.sleep(1)
        print(f'Square : {i*i}', end='\n')


def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube : {i*i*i}', end='\n')

if __name__ =="__main__":

    """ Create 2 process """
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)

    start_time = time.time()
    """ Start the process """
    p1.start()
    p2.start()

    """ Wait for the process to complete"""
    p1.join()
    p2.join()

    finish_time = time.time() - start_time
    print(finish_time)

    """Both this process will get executed in separate memory not like thread"""
