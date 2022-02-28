import multiprocessing as mp
import time


def fun(n):
    time.sleep(n)
    return n


pool = mp.Pool(1)
process = pool.apply_async(fun, (3,))
print("Start")
try:
    result = process.get(timeout=2)
except mp.context.TimeoutError:
    result = -1
print(result)
