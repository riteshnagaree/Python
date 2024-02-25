'''with open("readme.txt","r") as file:
	contents = file.read()

	
with open("writefile.txt","w") as file:
	file.write(contents)


print(contents)


input1 = input("Enter the string :")

with open("user_input.txt","w") as file:
	file.write(input1)

with open("user_input.txt","r") as file:
	contents = file.read()
'''

input1 = input("Enter the string :")

with open("example.txt","r") as file:
	read = file.read()

if read == input1:
	print("we have Same!")
	with open("example.txt","w") as file:
		file.write("Same")
else:
	print("input is Different!!!!")
	with open("user_input.txt","w") as file:
		file.write("Different!!")

