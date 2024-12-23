#printing only the numbers that are doubles of the numbers in list1


list1=[2,3,4,5,6]
list2=[4,8,10,20,18]
list3=[]
i=0
j=0
while(i<len(list1)):
    j=0
    while(j<len(list2)):
        if(list1[i]*2==list2[j]):
            list3.append(list2[j])
        j=j+1
    i=i+1
print(list3)
            
