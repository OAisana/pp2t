def has_33(a):
    for i in range(1,len(a)-1):
        if a[i] == 3 and a[i+1] == 3:
            return True
        else:
            return False
a = []
x=int(input())
for i in range(x):
    a.append(int(input()))
print(has_33(a))