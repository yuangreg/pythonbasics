import multiprocessing as mp
import time

def job(l, v, q, num):
    res = 0
    for _ in range(10):
        time.sleep(0.1)
        l.acquire() # Lock the shared memory before read and write
        v.value += num # Retrieve value of shared memory
        res += v.value
        print("job ", num, "update", v.value)
        l.release() # Release the lock for other process
    q.put(res)  # queue


def multicore():
    l = mp.Lock() # Lock
    v = mp.Value('i', 0) # Shared memory (Global variable not useful in multiprocessing)
    q = mp.Queue() # For return output
    p1 = mp.Process(target=job, args=(l, v, q, 1))
    p2 = mp.Process(target=job, args=(l, v, q, 2))
    p1.start() # Start p1
    p2.start() # Start p2
    p1.join()  # Wait for p1 to finish before continue
    p2.join()  # Wait for p1 to finish before continue
    res1 = q.get()
    res2 = q.get()
    print("Final Result ", res1 + res2)

if __name__ == '__main__':
    multicore()