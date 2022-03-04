import textdistance

def dist(s1, s2, s3):
    lev = textdistance.Levenshtein()
    return lev(s1, s2)

s1 = input()
s2 = input()
s3 = input()
res = dist(s1, s2, s3)

