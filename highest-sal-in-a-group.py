n=int(input())
l1_n=[]
l1_s=[]
max_name=''
max_sal=0
for i in range(n):
    name=input("Enter name: ")
    l1_n.append(name)
    sal=int(input("Enter salary: "))
    l1_s.append(sal)
max_sal=max(l1_s)
max_name=l1_n[l1_s.index(max_sal)]
print(f"{max_name} has highest salary of {max_sal}")



# output:
# 5
# Enter name: suma
# Enter salary: 20000
# Enter name: sarvani
# Enter salary: 15000
# Enter name: tejasri
# Enter salary: 100000
# Enter name: divya
# Enter salary: 30000
# Enter name: yasasini
# Enter salary: 40000
# tejasri has highest salary of 100000
