import multiprocessing
from multiprocessing import Pool
import time, ctypes

def first_func(array):
    for i in range(10):
        array.append(i)
        time.sleep(1)


def second_func(array):
    while 1:
        if len(array) > 0:
            print(array)
            for i in array:
                print(i)
                array.remove(i)
            time.sleep(3)

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    array = mgr.list()
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(first_func, args=[array])
    r2 = pool.apply_async(second_func, args=[array])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
    exit()