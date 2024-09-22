## Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time


def square_number(number):
    time.sleep(2)
    return number * number

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 64, 5]

    with ProcessPoolExecutor(max_workers=3) as executor:
        result = executor.map(square_number, numbers)
        
    for i in result:
        print(i)