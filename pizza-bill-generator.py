# Pricing details
normal_veg_price = 300
normal_nonveg_price = 400
deluxe_veg_price = 600
deluxe_nonveg_price = 800
extra_cheese_price = 100
extra_topping_price = 100
water_bottle_price = 20
ketchup_packet_price = 5
soft_drink_price = 75
takeaway_charge = 20
gst_rate = 0.18

# User selections
print("Pizza Categories\n1.Normal\n2.Deluxe")
category_choice = int(input("Enter your Choice [1 or 2]: "))
print("\nPizza Types\n1.Veg\n2.Non Veg")
type_choice = int(input("Enter your Choice [1 or 2]: "))

if category_choice == 1:
    base_price = normal_veg_price if type_choice == 1 else normal_nonveg_price
else:
    base_price = deluxe_veg_price if type_choice == 1 else deluxe_nonveg_price

# Add-ons
extra_cheese = int(input("\nExtra Cheese? [1.Yes or 2.NO]: "))
extra_topping = int(input("Extra Topping? [1.Yes or 2.NO]: "))
water_bottle = int(input("Do you want Water Bottles? [1.Yes or 2.NO]: "))
ketchup = int(input("Do you want Ketchup? [1.Yes or 2.NO]: "))
ketchup_packets = int(input("How many Packets? : ")) if ketchup == 1 else 0
soft_drinks = int(input("Do you want Soft Drinks? [1.Yes or 2.NO]: "))
takeaway = int(input("Is it a Take Away? [1.Yes or 2.NO]: "))

# Calculating add-on charges
total_cost = base_price
if extra_cheese == 1:
    total_cost += extra_cheese_price
if extra_topping == 1:
    total_cost += extra_topping_price
if water_bottle == 1:
    total_cost += water_bottle_price
total_cost += ketchup_packets * ketchup_packet_price
if soft_drinks == 1:
    total_cost += soft_drink_price
if takeaway == 1:
    total_cost += takeaway_charge

# Calculating GST and net amount
gst = total_cost * gst_rate
net_amount = total_cost + gst

# Printing bill
print("\n-----------------------------------------")
print("***** Pizza Bill Generator *****")
print("-----------------------------------------")
print("Base Price                = ", base_price)
if extra_cheese == 1:
    print("Extra Cheese            = ", extra_cheese_price)
if extra_topping == 1:
    print("Extra Toppings         = ", extra_topping_price)
if water_bottle == 1:
    print("Water Bottle            = ", water_bottle_price)
if ketchup_packets > 0:
    print("Ketchup Packets       = ", ketchup_packets * ketchup_packet_price)
if soft_drinks == 1:
    print("Soft Drinks              = ", soft_drink_price)
if takeaway == 1:
    print("Take Away Charges  = ", takeaway_charge)
print("-----------------------------------------")
print("Total Cost                 = ", total_cost)
print("GST Charges             = ", round(gst, 2))
print("-----------------------------------------")
print("Net Amount Payable   = ", round(net_amount, 2))










# output:
# Pizza Categories
# 1.Normal
# 2.Deluxe
# Enter your Choice [1 or 2]: 2

# Pizza Types
# 1.Veg
# 2.Non Veg
# Enter your Choice [1 or 2]: 2

# Extra Cheese? [1.Yes or 2.NO]: 1
# Extra Topping? [1.Yes or 2.NO]: 1
# Do you want Water Bottles? [1.Yes or 2.NO]: 1
# Do you want Ketchup? [1.Yes or 2.NO]: 1
# How many Packets? : 2
# Do you want Soft Drinks? [1.Yes or 2.NO]: 1
# Is it a Take Away? [1.Yes or 2.NO]: 2

# -----------------------------------------
# ***** Pizza Bill Generator *****
# -----------------------------------------
# Base Price                =  800
# Extra Cheese            =  100
# Extra Toppings         =  100
# Water Bottle            =  20
# Ketchup Packets       =  10
# Soft Drinks              =  75
# -----------------------------------------
# Total Cost                 =  1105
# GST Charges             =  198.9
# -----------------------------------------
# Net Amount Payable   =  1303.9
