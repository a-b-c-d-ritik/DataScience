import multiprocessing;
#import multiprocessing.process
import time

def sq_no():
    for i in range(5):
        time.sleep(2)
        print(f"sq of {i}={i*i}")

def cube_no():
    for i in range(5):
        time.sleep(2)
        print(f"cube of {i}={i*i*i}")


if __name__=="__main__":
    p1=multiprocessing.Process(target=sq_no)
    p2=multiprocessing.Process(target=cube_no)
    t=time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish_time=time.time()-t
    print(finish_time)