## Multi threading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    print(f"Number: {number}")  
    
 
numbers = [1,2,3,4,5,6,7,8,9,99,64,5]    
with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(print_number, numbers)
    
for i in result:
    print(i)
