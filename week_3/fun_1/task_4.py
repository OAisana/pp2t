num = []
prime_num = []
def filter_prime():
     for i in num:
         count_divider = 0
         for j in range(1, i): 
             if i % j == 0:
                 count_divider += 1
         if count_divider == 1:
             prime_num.append(i)
     print(prime_num)

x = int(input())
for i in range (x):
    num.append(int(input()))

filter_prime()
