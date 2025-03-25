# Check whether the given num is positive or negative without using >,<,>=,<=,==.

n=int(input())
if abs(n)==n:
    print("positive")
else:
    print("negative")
