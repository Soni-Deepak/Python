'''

Sum(0) = 1
Sum(1) = 1
Sum(5) = 5 + 4 + 3 + 2 + 1
Sum(n) = n + (n-1) + ......  + 4 + 3 + 2 + 1


Sum(n) = n + Sum(n-1)


'''

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

print(sum(4))    