import itertools

def slide(seq, n):
    i = 0
    while True:
        it = itertools.islice(itertools.tee(seq, 1)[0], i, i+n)
        nxt = next(it, None)
        if nxt is None:
            break
        else:
            yield nxt
        yield from it
        i += 1

import sys
exec(sys.stdin.read())
