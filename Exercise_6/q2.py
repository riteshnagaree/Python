def calculator(num1,num2,operator):

	if operator == '+':

		return num1+num2
	elif operator == '-':
		return num1-num2
	elif operator == '/':
	
		return num1/num2
	else:
		print("Choose +,-,/")


def accept_input():
	num1 = int(input("Enter the  numbers :"))
	num2 = int(input("Enter the  2nd number :"))
	operator = input("Enter the operator +,-,/:")
	

	return num1,num2,operator


num1, num2, operator = accept_input()
res = calculator(num1,num2,operator)
print("the result is",res)



