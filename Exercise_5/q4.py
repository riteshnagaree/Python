
numbr1=int(input("Enter the 1st number: "))
numbr2=int(input("Enter the 2nd number: "))
numbr3=int(input("Enter the 3rd number: "))


if numbr1 > numbr2 and numbr1 > numbr3:
	print(f"{numbr1} is greater")

elif numbr2 > numbr3 and numbr2 > numbr1:
	print(f"{numbr2} is greater")

else:
	print(f"{numbr3} is greater")