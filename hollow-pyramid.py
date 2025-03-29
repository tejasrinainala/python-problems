n=int(input())
for i in range(n):
    for j in range(n,i+1,-1):
        print(" ",end=" ")
    for j in range((i*2)+1):
        if i==n-1:
            print('*',end=" ")
        else:
            if(j==0 or j>=i*2):
                print('*',end=" ")
            else:
                print(" ",end=" ")
                
    print()


# output:
# 4
#       * 
#     *   * 
#   *       * 
# * * * * * * * 
