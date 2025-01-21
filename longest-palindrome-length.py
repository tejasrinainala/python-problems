import math
phrase="aa abb xyxz xyyx abxba"
str_list=phrase.split(' ')
c=0
pali=[]
pali_len=[]
for i in str_list:
    l=0
    r=len(i)-1
    if l<r:
        if i[l]!=i[r]:
            continue
        else:
            c+=1 
        l+=1 
        r-=1
        pali.append(i)
for i in pali:
    pali_len.append(len(i))
length=max(pali_len)
print(math.factorial(length))
