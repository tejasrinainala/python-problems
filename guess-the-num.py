import random
n= random.randint(1, 20)
attempt= 0
print("Guess a number between 1 and 20.")

while True:
    g= int(input("Enter your guess: "))
    attempt=attempt+1
   
    if g < n:
        print("Too low! Try again.")
    elif g > n:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {n} in {attempt} attempts.")
        break
