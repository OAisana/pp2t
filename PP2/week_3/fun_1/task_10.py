def unique_element(a):
    new_a = []
    for i in range(len(a)):
        if i not in new_a:
            new_a.append(a[i])
    return new_a
ar=[]
a = int(input())
for i in range(a):
    ar.append(int(input()))
print(unique_element(ar))
