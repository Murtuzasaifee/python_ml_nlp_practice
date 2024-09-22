import multiprocessing
import sys
import math

sys.set_int_max_str_digits(100000)

def factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == '__main__':
    
    numbers = [2000,1999,4000]
    
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial,numbers)
        
