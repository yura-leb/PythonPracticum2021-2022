import textdistance

def dist(s1, s2):
    lev = textdistance.Levenshtein()
    return lev(s1, s2)

