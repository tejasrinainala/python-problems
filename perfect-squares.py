'''
Write a Python program to takes a range and creates a list of all numbers in the range which are perfect squares, and the sum of their digits is less than 10.
'''




F=[]
L=[]
l=int(input("Enter lower range:"))
u=int(input("Enter upper range:"))
while(l<=u):
    for i in range(1,l+1):
        if l%i==0:
            L.append(i)
    if len(L)%2==1:
        F.append(l)
    l=l+1
    L.clear()
print(F)
