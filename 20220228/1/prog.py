import textdistance
import multiprocessing as mp

def dist(s1, s2, s3):
    if s3 == "L":
        distance = textdistance.Levenshtein()
    elif s3 == "D":
        distance = textdistance.DamerauLevenshtein()
    else:
        return -1
    return distance(s1, s2)

s1 = input().strip('\n')
s2 = input().strip('\n')
s3 = input().strip('\n')
with mp.Pool(processes=1) as pool:
    proc = pool.apply_async(dist, (s1, s2, s3))
    print(proc.get())
