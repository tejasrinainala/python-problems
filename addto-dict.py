# Write a Python program to add the following values to the existing dictionary:

# Input:
# {"Name":"Sairam","Age":35,"Location":"Chennai"}
# Now we need to add – Qualification = M.Tech and Designation = Software Engineer to the already created dictionary.

  
  
  
dict = {"Name":"Sairam","Age":35,"Location":"Chennai"}

dict.update({"Qualification" : "M.Tech","Designation" : "Software Engineer"})

print(dict)
