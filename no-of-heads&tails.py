# Random Coin Flip Simulator

# Description:
# This program simulates flipping a coin a specified number of times and counts the number of heads and tails.







import random
n=int(input("Enter no of times you want to flip the coin : "))
heads=random.randint(1,n)
tails=n-heads
print(F"Results of flipping the coin {n} times: Heads-{heads},Tails-{tails}")


