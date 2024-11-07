number = int(input())
n = number

while n != 1 and n != 4:
    s = 0
    while n > 0:
        r = n % 10
        s += r * r
        n //= 10
    n = s

if n == 1:
    print(f"{number} is a Happy Number!")
else:
    print(f"{number} is not a Happy Number")
