
normal_veg_price = 300
normal_non_veg_price = 400
deluxe_veg_price = 600
deluxe_non_veg_price = 800

extra_cheese_price = 100
extra_topping_price = 100
water_bottle_price = 20
ketchup_packet_price = 5
soft_drink_price = 75
take_away_charge = 20


gst_rate = 0.18


print("Pizza Categories")
print("1.Normal\n2.Deluxe")
pizza_category = int(input("Enter your Choice [1 or 2]: "))

print("\nPizza Types")
print("1.Veg\n2.Non Veg")
pizza_type = int(input("Enter your Choice [1 or 2]: "))

extra_cheese = int(input("\nExtra Cheese? [1.Yes or 2.NO]: "))
extra_topping = int(input("Extra Topping? [1.Yes or 2.NO]: "))
water_bottle = int(input("\nDo you want Water Bottles? [1.Yes or 2.NO]: "))
if water_bottle == 1:
    water_bottle_count = int(input("How many Bottles? : "))
else:
    water_bottle_count = 0

ketchup = int(input("\nDo you want Ketchup? [1.Yes or 2.NO]: "))
if ketchup == 1:
    ketchup_count = int(input("How many Packets? : "))
else:
    ketchup_count = 0

soft_drink = int(input("\nDo you want Soft Drinks? [1.Yes or 2.NO]: "))
if soft_drink == 1:
    soft_drink_count = int(input("How many Cans? : "))
else:
    soft_drink_count = 0

take_away = int(input("\nIs it a Take Away? [1.Yes or 2.NO]: "))


if pizza_category == 1:  
    base_price = normal_veg_price if pizza_type == 1 else normal_non_veg_price
else:  
    base_price = deluxe_veg_price if pizza_type == 1 else deluxe_non_veg_price


extra_cheese_cost = extra_cheese_price if extra_cheese == 1 else 0
extra_topping_cost = extra_topping_price if extra_topping == 1 else 0
water_bottle_cost = water_bottle_count * water_bottle_price
ketchup_cost = ketchup_count * ketchup_packet_price
soft_drink_cost = soft_drink_count * soft_drink_price
take_away_cost = take_away_charge if take_away == 1 else 0


total_cost = (base_price + extra_cheese_cost + extra_topping_cost +
              water_bottle_cost + ketchup_cost + soft_drink_cost + take_away_cost)
gst_charges = total_cost * gst_rate
net_amount_payable = total_cost + gst_charges


print("\n-----------------------------------------")
print("***** Pizza Bill Generator *****")
print("-----------------------------------------")
print(f"Base Price                = {base_price}")
if extra_cheese_cost > 0:
    print(f"Extra Cheese            = {extra_cheese_cost}")
if extra_topping_cost > 0:
    print(f"Extra Toppings         = {extra_topping_cost}")
if water_bottle_cost > 0:
    print(f"Water Bottles          = {water_bottle_cost}")
if ketchup_cost > 0:
    print(f"Ketchup Packets       = {ketchup_cost}")
if soft_drink_cost > 0:
    print(f"Soft Drinks            = {soft_drink_cost}")
if take_away_cost > 0:
    print(f"Take Away Charges  = {take_away_cost}")
print("-----------------------------------------")
print(f"Total Cost                 = {total_cost}")
print(f"GST Charges             = {gst_charges:.1f}")
print("-----------------------------------------")
print(f"Net Amount Payable   = {net_amount_payable:.1f}")
