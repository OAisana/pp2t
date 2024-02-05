def histogram(numb):
    for num in numb:
        print('*' * num)
        
a = []

x=int(input())
for i in range(x):
    a.append(int(input()))
histogram(a)


