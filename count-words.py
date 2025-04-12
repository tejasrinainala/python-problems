s=input()
c=0
res=''
ar=[]
for i in range(len(s)):
    res+=s[i]
    if s[i]==' ':
        c+=1
        ar.append(res)
        res=''
if res: 
    ar.append(res)
    c+=1
print(c)
print(ar)



# output:
# ongole is in andhrapradesh in india
# 6
# ['ongole ', 'is ', 'in ', 'andhrapradesh ', 'in ', 'india']
