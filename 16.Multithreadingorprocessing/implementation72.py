import multiprocessing
import math
import sys
import time

#increase the maximum no of digits for integer conversion
sys.setintmaxstrdigits(100000)

#fn to compute factorials of a given no
def computer_fact(no):
    print(f"computing factorial of {no}",math.factorial(no))
    return math.factorial(no)


if __name__=="__main__":
    numbers=[50000,6000,1254,5]
    start_time=time.time()
    #creating pool of worker process
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_fact,numbers)

end_time=time.time()
print("time taken=",start_time-end_time)
