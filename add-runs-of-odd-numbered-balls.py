runs=input("Enter runs in over : ").split(" ")
s=list(runs)
add=0
for i in range(len(s)):
    if i%2==0:
        add+=int(s[i])
print("The sum of runs in odd balls is ",add)
    
#  output:
# Enter runs in over : 1 3 5 7 9 10
# The sum of runs in odd balls is  15
