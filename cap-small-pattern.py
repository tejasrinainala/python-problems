 # Alphabet pattern where for even column capital letters and odd column small letters should print.


k1=65
k2=98
for i in range(5):
    for j in range(i+1):
        if i%2==0:
            print(chr(k1),end=" ")
            k1+=1
            if i!=0:
                k2+=1
        else:
            print(chr(k2),end=" ")
            k2+=1
            k1+=1
    print()


#output
# A 
# b c 
# D E F 
# g h i j 
# K L M N O
