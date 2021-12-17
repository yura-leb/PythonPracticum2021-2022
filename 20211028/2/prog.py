import itertools

def slide(seq, n):
    dup = seq
    while True:
        dup, seq = itertools.tee(dup)
        current = list(itertools.islice(seq, n))
        if not current:
            break
        yield from current
        next(dup)

import sys
exec(sys.stdin.read())
