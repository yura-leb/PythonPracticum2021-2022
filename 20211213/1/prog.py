import random
import asyncio
from collections import defaultdict
import math

L = list(range(16))
random.shuffle(L)
LL = L.copy()

async def merge(b0, b1, e1, n, event_b0_e0, event_b1_e1, event_b0_e1):
    b, e0, i = b0, b1, b0
    await event_b0_e0.wait()
    await event_b1_e1.wait()
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(0.1)
    print(f"> {n}")
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    event_b0_e1.set()


async def joiner():
    n = 0
    tasks = []
    done_event = asyncio.Event()
    done_event.set()
    events = dict()

    for p in range(4):
        b = 2**(p+1)
        for i in range(0, len(L), b):
            events[(i, i+b)] = asyncio.Event()
    print(events.keys())
    
    for p in range(4):
        b = 2**(p+1)
        for i in range(0, len(L), b):
            if b == 2:    
                tasks.append(asyncio.create_task(merge(i, i+b//2, i+b, n, done_event, done_event, events[(i, i+b)])))
            else:
                tasks.append(asyncio.create_task(merge(i, i+b//2, i+b, n, events[(i, i + b//2)], events[(i+b//2, i+b)], events[(i, i+b)])))
            n += 1
    await asyncio.gather(*tasks)

asyncio.run(joiner())    
print(L)



    

##import sys
##exec(sys.stdin.read())
