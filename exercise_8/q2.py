
# Regular expr printing in 9,99,999 formatt

import re

while True:
	amount = input("enter the amount in the format 9,99,999 : ")
	if re.match(r'^\d{1},\d{2},\d{3}$', amount):
		break
	else:
		print("Please enetr in correct formatt !!!")

print("You entered amount is : ",amount)