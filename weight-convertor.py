weight=int(input("Weight: "))
convert=input("(K)gs or (L)bs : ")
if convert == 'k' or convert =='K':
    print("Weight in lbs : ",(weight/0.45))
elif convert == 'L' or convert == 'l':
    print("Weight in kg : ",(weight*0.45))
    

