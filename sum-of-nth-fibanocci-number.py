n=int(input())
n1=0
n2=1
n3=n1+n2
c=n1+n2+n3
if n==1:
    print(0)
elif n==2:
    print(1)
elif n==3:
    print(c)
else:
    for i in range(n-3):
        n1=n2
        n2=n3
        n3=n1+n2
        c+=n3
    print(c)




# input:
# 10
# output:
# 88
