list1=["mon","jan","app","pan"]
list2=["da","le","uary","day"]
list3=[]
x=0
y=len(list2)-1
while(x<len(list1)):
    while(y>=0):
        list3.append(list1[x]+list2[y])
        y=y-1
        x=x+1
print(list3)

        
