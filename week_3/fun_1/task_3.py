numh = int(input())
numl = int(input())

def solve (h,l):
    rab_h = int ((l-2*h)/2)
    chicken_h = int(h-rab_h)
    print(rab_h, chicken_h)

solve(numh, numl) 