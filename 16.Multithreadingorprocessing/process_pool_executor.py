#multithreading with process pool executor

from concurrent.futures import ProcessPoolExecutor
import multiprocessing.connection
import time

def sq_no(no):
        time.sleep(2)
        return (f"sq of {no}={no*no}")

numbers=[1,2,3,4,5]

if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        result=executor.map(sq_no,numbers)

for r in result:
    print(r)