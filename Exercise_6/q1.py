

def calculator(num1,num2,operator):

	if operator == '+':

		return num1+num2
	elif operator == '-':
		return num1-num2
	elif operator == '/':
	
		return num1/num2
	else:
		print("Choose +,-,/")




res= calculator(5,6,'+')
print("The add result is ",res)

res= calculator(15,6,'-')
print("The  diff result is ",res)

res= calculator(150,6,'/')
print("The  div result is ",res)

res= calculator(150,6,'_')
print("The invalid result is ",res)