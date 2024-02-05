def palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False
a=str(input())
print(palindrome(a))
