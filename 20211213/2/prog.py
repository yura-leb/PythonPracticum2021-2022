import random
import asyncio
from collections import defaultdict
import math

L = eval(input())
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
    await asyncio.sleep(0)
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    event_b0_e1.set()


async def joiner():
    n = 0
    tasks = []
    done_event = asyncio.Event()
    done_event.set()
    events = dict()
    two_power = math.ceil(math.log2(len(L)))
                          
    for p in range(two_power):
        b = 2**(p+1)
        for i in range(0, len(L), b):
            if i+b <= len(L):
                events[(i, i+b)] = asyncio.Event()
            else:
                if i < len(L):
                    events[(i, len(L))] = asyncio.Event()
                    
    for p in range(two_power):
        b = 2**(p+1)
        for i in range(0, len(L), b):
            if b == 2:
                if i+b <= len(L):
                    tasks.append(asyncio.create_task(merge(i, i+b//2, i+b, n, done_event, done_event, events[(i, i+b)])))
                else:
                    if i < len(L):
                        tasks.append(asyncio.create_task(merge(i, len(L)-1, len(L), n, done_event, done_event, events[(i, len(L))])))
            else:
                if i+b <= len(L):
                    tasks.append(asyncio.create_task(merge(i, i+b//2, i+b, n, events[(i, i + b//2)], events[(i+b//2, i+b)], events[(i, i+b)])))
                else:
                    if i < len(L) and i+b//2 < len(L):
                        tasks.append(asyncio.create_task(merge(i, i+b//2, len(L), n, events[(i, i + b//2)], events[(i+b//2, len(L))], events[(i, len(L))])))
                        
            n += 1
    await asyncio.gather(*tasks)

asyncio.run(joiner())    
print(L)

