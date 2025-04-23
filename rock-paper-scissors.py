#rock paper and scissors with computer.



import random
choices=['rock','paper','scissors']
comp=random.choice(choices)
user=input().lower()
if comp==user:
    print("Draw")
elif (comp=='rock' and user=='paper') or  (user=='rock' and comp=='scissors') or (comp=='paper' and user=='scissors'):
    print("User won!")
elif (user=='rock' and comp=='paper') or (comp=='rock' and user=='scissors') or (user=='paper' and comp=='scissors'):
    print("Computer won!")
else:
    print("Enter valid input.")



    

    
