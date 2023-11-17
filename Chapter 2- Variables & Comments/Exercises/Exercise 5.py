total_money = 50  
usb_stick_price = 6  

num_usb_sticks = total_money // usb_stick_price
remaining_money = total_money % usb_stick_price

print(f"Her purchase of {num_usb_sticks} USB sticks will cost her £{total_money}.")
print(f"After the purchase, she will have £{remaining_money} remaining.")