'''
Sum(1) = 1
Sum(2) = 1 + 2
Sum(3) = 1 + 2 + 3
Sum(4) = 1 + 2 + 3 + 4
Sum(n) = 1 + 2 + 3 +......n -1 + n

Sum(n) = Sum(n-1) + n 
'''
def sum(n):
    if(n ==1):
        return 1
        return sum(n-1) + n
print(sum(4))