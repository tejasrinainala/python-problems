s="ZOHOCORPORATIONTEAM"
n=7
k=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or i==1 or i+j==n+1:
            print(s[k],end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
    



# output:
# Z O H O C O R 
#           P   
#         O     
#       R       
#     A         
#   T           
# I O N T E A M 
