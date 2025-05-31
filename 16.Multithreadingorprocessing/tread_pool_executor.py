#multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(no):
    time.sleep(1)
    return (f"no:{no}")

no=[1,2,3,4.5]

with ThreadPoolExecutor(max_workers=3) as executor:
    res=executor.map(print_number,no)

for result in res:
    print(result)