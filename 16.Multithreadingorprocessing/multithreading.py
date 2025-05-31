import threading;
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"no:{i}")

def print_letters():
    for i in "abcdef":
        time.sleep(2)
        print(f"letters:{i}")


#creating threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)




t=time.time()
t1.start()
t2.start()
print_numbers()
print_letters()

t1.join()
t2.join()
finish_time=time.time()-t
print(finish_time)