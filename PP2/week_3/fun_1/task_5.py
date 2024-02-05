import itertools

def strP():
    word = input()
    perm = permission(word)
    for i in list(perm):
        print(i)

strP()