from concurrent.futures import ProcessPoolExecutor
import time


def print_number(numbers):
    time.sleep(1)
    return f'Number : {numbers}'


numbers = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4]

if __name__ == '__main__':

    start_time = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number, numbers)

    for i in results:
        print(i)

    finish_time = time.time() - start_time
    print(finish_time)