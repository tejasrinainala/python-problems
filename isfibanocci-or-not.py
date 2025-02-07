def is_fibonacci(n):
    if n < 0:
        return False
    n1, n2 = 0, 1
    while n1 <= n:
        if n1 == n:
            return True
        n1, n2 = n2, n1 + n2
    return False

n = int(input("Enter a number: "))
print(is_fibonacci(n))



# output:
# Enter a number: 5
# True
