k=0
k1='A'
k2='b'
for i in range(5):
    for j in range(5):
        if k%2==0:
            print(k1,end=" ")
            k1=chr(ord(k1)+2)
        else:
            print(k2,end=" ")
            k2=chr(ord(k2)+2)
        k += 1
    print()


#output
# A 
# b C 
# d E f 
# G h I j 
# K l M n O 
