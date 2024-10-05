import random
n=int(input("Enter no of times you want to flip the coin : "))
heads=random.randint(1,n)
tails=n-heads
print(F"Results of flipping the coin {n} times: Heads-{heads},Tails-{tails}")


