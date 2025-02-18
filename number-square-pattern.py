# Input: N = 4
# Output:
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4



n=int(input())
size=2*n-1
min_dis=0
for i in range(size):
    for j in range(size):
        min_dis=min(i,j,size-1-i,size-1-j)
        print(n-min_dis,end=" ")
    print()
