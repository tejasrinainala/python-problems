import random
n=random.randint(0,20)
i=0
while True:
        m=int(input("Enter a number : "))
        i+=1
        if n>m:
            print("The number is too low!")
        elif n<m:
            print("The number is too high!")
        else:
            print(F"Hurray! you guessed the number correctly in {i} attempts")
            break
            

